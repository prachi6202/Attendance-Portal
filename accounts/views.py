from django.shortcuts import render
from .forms import UserForm,UserProfileInfoForm,teacher_timetableform
from .models import *
# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import student_tymtable,teacher_timetable
from django.contrib.auth.decorators import login_required
# Create your views here.

def home(request):
    items = UserProfileInfo.objects.all()
    user = request.user
    # if user:
    x = int(user.id)-18

    table = student_tymtable.objects.filter(specialization=request.user.userprofileinfo.specialization,class_grp=request.user.userprofileinfo.class_grp)
    first_link=teacher_timetable.objects.filter(name=student_tymtable.First_lech_teacher)
    print(first_link)
    #catprods =.objects.values('category')
    #cats = {item['category'] for item in catprods}
    #for cat in cats:
     #   prod = Product.objects.filter(category=cat)
    context = {
        'roll': items[x].rollnumber,
        'course': items[x].specialization,
        'table':table,
        'first_link':first_link,
    }
    print(context)
    print(items)
    print(items[1],items[2],items[3])
    print(table)
    return render(request, 'accounts/home.html',context)

def index(request):
    return render(request, 'accounts/index.html')
def about(request):
    return render(request,'accounts/about.html')

@login_required
def special(request):
    return HttpResponse("You are logged in. Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))

def register(request):

    registered = False

    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid():

            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

            registered = True
            return render(request, 'accounts/login.html',{'name':user.username})

        else:
            print(user_form.errors,profile_form.errors)

    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()

    return render(request,'accounts/registration.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})


def user_login(request):

    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')


        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            if user.is_active:
                if user.is_staff:
                    return HttpResponseRedirect(reverse('tymtable'))

                else:
                    return HttpResponseRedirect(reverse('home'))

            else:
                return HttpResponse("Your account is not active.")
        else:
            print("Someone tried to login and failed.")
            print("They used username: {} and password: {}".format(username,password))
            return HttpResponse("Invalid login details supplied.")

    else:
        return render(request, 'accounts/login.html', {})

def tymtable(request):
    all_teacher=teacher_timetable.objects.filter(user=request.user)
    print(all_teacher)
    return render(request, 'accounts/tymtable.html',{'all_teacher': all_teacher})



def delete(request,id):
    pk=id
    teacher_timetable.objects.filter(id=pk).delete()

    return HttpResponseRedirect(reverse('tymtable'))

def update(request,id):
    print('h1')
    pk=id
    teacher=teacher_timetable.objects.get(id=pk)
    print('h2')
    form=teacher_timetableform(instance=teacher)
    print('h3')
    if request.method=='POST':
        form=teacher_timetableform(request.POST,instance=teacher)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('tymtable'))
    else:
        context={'form':form,'id':id}
        print('h4')
        return render(request,'accounts/edit.html',context)