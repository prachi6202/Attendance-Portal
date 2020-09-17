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
    all_teacher=[]
    a=[]
    b=[]
    c=[]
    d=[]
    e=[]
    f=[]
    g=[]
   # table=[]
    #print(type(table))
    table = student_tymtable.objects.filter(specialization=request.user.userprofileinfo.specialization,class_grp=request.user.userprofileinfo.class_grp)
    for t in table:
        t1=teacher_timetable.objects.filter(name=t.First_lech_teacher,day=t.day)
        a.append(t1)
        t2=teacher_timetable.objects.filter(name=t.sec_lech_teacher,day=t.day)
        b.append(t2)
        t3 = teacher_timetable.objects.filter(name=t.third_lech_teacher,day=t.day)
        c.append(t3)
        t4 = teacher_timetable.objects.filter(name=t.fourth_lech_teacher,day=t.day)
        d.append(t4)
        t5 = teacher_timetable.objects.filter(name=t.fifth_lech_teacher,day=t.day)
        e.append(t5)
        t6 = teacher_timetable.objects.filter(name=t.sixth_lech_teacher,day=t.day)
        f.append(t6)
        t7 = teacher_timetable.objects.filter(name=t.sev_lech_teacher,day=t.day)
        g.append(t7)


    context = {
        'roll': items[x].rollnumber,
        'course': items[x].specialization,
        'table':table,
        'a':a,
        'b':b,
        'c':c,
        'd':d,
        'e':e,
        'f':f,
        'g':g,

    }


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