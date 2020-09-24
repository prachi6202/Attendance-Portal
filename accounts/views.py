from django.shortcuts import render
from .forms import UserForm,UserProfileInfoForm,teacher_timetableform
from .models import *
# Extra Imports for the Login and Logout Capabilities
from django.contrib.auth import authenticate, login as django_login ,logout as django_logout
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from .models import student_tymtable,teacher_timetable
from django.contrib.auth.decorators import login_required
# Create your views here.
@login_required
def home(request):
    items = UserProfileInfo.objects.all()
    user = request.user
    # if user:
    x = int(user.id)-18
    all_teacher=[]
    a1=[]
    b1=[]
    b2=[]
    b3=[]
    b4=[]
    b5=[]
    b6=[]
    a2 = []
    a3 = []
    a4 = []
    a5 = []
    a6 = []
    c1 = []
    c2 = []
    c3 =[]
    c4 =[]
    c5 =[]
    c6 =[]
    d1 = []
    d2 = []
    d3 = []
    d4 = []
    d5 = []
    d6 = []
    e1 = []
    e2 = []
    e3 = []
    e4 = []
    e5 = []
    e6 = []
    f1 = []
    f2 = []
    f3 = []
    f4 = []
    f5 = []
    f6 = []
    g1 = []
    g2 = []
    g3 = []
    g4 = []
    g5 = []
    g6 = []

    table = student_tymtable.objects.filter(specialization=request.user.userprofileinfo.specialization,class_grp=request.user.userprofileinfo.class_Group)
    # code for 1st lecture of every day
    name=student_tymtable.objects.values('First_lech_teacher')
    cats={item['First_lech_teacher'] for item in name}
    print(cats)
    k1=[]
    kx=[]
    n1=[]
    n2=[]
    n3=[]
    n4=[]
    for cat in cats:
        x1=student_tymtable.objects.filter(First_lech_teacher=cat,day='Monday')
        for k in x1:
            k1.append(k.First_lech_teacher)
            print(k1)
        x2 = student_tymtable.objects.filter(First_lech_teacher=cat, day='Tuesday')
        for k2 in x2:
            kx.append(k2.First_lech_teacher)
        x3 = student_tymtable.objects.filter(First_lech_teacher=cat, day='Wednesday')
        for k3 in x3:
            n1.append(k3.First_lech_teacher)
        x4 = student_tymtable.objects.filter(First_lech_teacher=cat, day='Thursday')
        for k4 in x4:
            n2.append(k4.First_lech_teacher)
        x5 = student_tymtable.objects.filter(First_lech_teacher=cat, day='Friday')
        for k5 in x5:
            n3.append(k5.First_lech_teacher)
        x6 = student_tymtable.objects.filter(First_lech_teacher=cat, day='Saturday')
        for k6 in x6:
            n4.append(k6.First_lech_teacher)


    for q1 in k1:
        t1=teacher_timetable.objects.filter(name=q1,day='Monday')
        print(t1)
        for s1 in t1:
            l1=s1.First_link
            print(l1)
            a1.append(l1)
    for q in kx:
        t2 = teacher_timetable.objects.filter(name=q, day='Tuesday')
        for s2 in t2:
            l2=s2.First_link
            a2.append(l2)
    for q in n1:
        t3 = teacher_timetable.objects.filter(name=q, day='Wednesday')
        for s3 in t3:
            l3=s3.First_link
            a3.append(l3)
    for q in n2:
        t4 = teacher_timetable.objects.filter(name=q, day='Thursday')
        for s4 in t4:
            l4 = s4.First_link
            a4.append(l4)
    for q in n3:
        t5 = teacher_timetable.objects.filter(name=q, day='Friday')
        for s5 in t5:
            l5 = s5.First_link
            a5.append(l5)
    for q in n4:
        t6 = teacher_timetable.objects.filter(name=q, day='Saturday')
        for s6 in t6:
            l6 = s6.First_link
            a6.append(l6)
    # code for 2nd lecture of every day

    name1 = student_tymtable.objects.values('sec_lech_teacher')
    cats1 = {item['sec_lech_teacher'] for item in name1}
    print(cats)
    n5=[]
    n6=[]
    n7=[]
    n8=[]
    n9=[]
    n10=[]
    for cat in cats1:
        y1 = student_tymtable.objects.filter(sec_lech_teacher=cat, day='Monday')
        for k in y1:
            n5.append(k.sec_lech_teacher)
        y2 = student_tymtable.objects.filter(sec_lech_teacher=cat, day='Tuesday')
        for k2 in y2:
            n6.append(k2.sec_lech_teacher)
        y3 = student_tymtable.objects.filter(sec_lech_teacher=cat, day='Wednesday')
        for k3 in y3:
            n7.append(k3.sec_lech_teacher)
        y4 = student_tymtable.objects.filter(sec_lech_teacher=cat, day='Thursday')
        print(y4)
        for k4 in y4:
            n8.append(k4.sec_lech_teacher)
            print(n8)
        y5 = student_tymtable.objects.filter(sec_lech_teacher=cat, day='Friday')
        for k5 in y5:
            n9.append(k5.sec_lech_teacher)
        y6 = student_tymtable.objects.filter(sec_lech_teacher=cat, day='Saturday')
        for k6 in y6:
            n10.append(k6.sec_lech_teacher)
    for q in n5:
        t21 = teacher_timetable.objects.filter(name=q, day='Monday')
        print(t1)
        for s1 in t21:
            l1 = s1.second_link
            b1.append(l1)
    for q in n6:
        t22 = teacher_timetable.objects.filter(name=q, day='Tuesday')
        for s2 in t22:
            l2 = s2.second_link
            b2.append(l2)
    for q in n7:
        t23 = teacher_timetable.objects.filter(name=q, day='Wednesday')
        for s3 in t23:
            l3 = s3.second_link
            b3.append(l3)
    for q in n8:
        t24 = teacher_timetable.objects.filter(name=q, day='Thursday')
        print(t24)
        for s4 in t24:
            l4 = s4.second_link
            print(l4)
            b4.append(l4)
    for q in n9:
        t25 = teacher_timetable.objects.filter(name=q, day='Friday')
        for s5 in t25:
            l5 = s5.second_link
            b5.append(l5)
    for q in n10:
        t26 = teacher_timetable.objects.filter(name=q, day='Saturday')
        for s6 in t26:
            l6 = s6.second_link
            b6.append(l6)
            # code for 3rd lecture of every day

    name2 = student_tymtable.objects.values('third_lech_teacher')
    cats2 = {item['third_lech_teacher'] for item in name2}
    cp1=[]
    cp2=[]
    cp3=[]
    cp4=[]
    cp5=[]
    cp6=[]
    print(cats)
    for cat in cats2:
        u1 = student_tymtable.objects.filter(third_lech_teacher=cat, day='Monday')
        for k in u1:
            cp1.append(k.third_lech_teacher)
        u2 = student_tymtable.objects.filter(third_lech_teacher=cat, day='Tuesday')
        for k2 in u2:
            cp2.append(k2.third_lech_teacher)
        u3 = student_tymtable.objects.filter(third_lech_teacher=cat, day='Wednesday')
        for k3 in u3:
            cp3.append(k3.third_lech_teacher)
        u4 = student_tymtable.objects.filter(third_lech_teacher=cat, day='Thursday')
        for k4 in u4:
            cp4.append(k4.third_lech_teacher)
        u5 = student_tymtable.objects.filter(third_lech_teacher=cat, day='Friday')
        for k5 in u5:
            cp5.append(k5.third_lech_teacher)
        u6 = student_tymtable.objects.filter(third_lech_teacher=cat, day='Saturday')
        for k6 in u6:
            cp6.append(k6.third_lech_teacher)
    for q in cp1:
        t31 = teacher_timetable.objects.filter(name=q, day='Monday')
        print(t1)
        for s1 in t31:
            l1 = s1.third_link
            c1.append(l1)
    for q in cp2:
        t32 = teacher_timetable.objects.filter(name=q, day='Tuesday')
        for s2 in t32:
            l2 = s2.third_link
            c2.append(l2)
    for q in cp3:
        t33 = teacher_timetable.objects.filter(name=q, day='Wednesday')
        for s3 in t33:
            l3 = s3.third_link
            c3.append(l3)
    for q in cp4:
        t34 = teacher_timetable.objects.filter(name=q, day='Thursday')
        for s4 in t34:
            l4 = s4.third_link
            c4.append(l4)
    for q in cp5:
        t35 = teacher_timetable.objects.filter(name=q, day='Friday')
        for s5 in t35:
            l5 = s5.third_link
            c5.append(l5)
    for q in cp6:
        t36 = teacher_timetable.objects.filter(name=q, day='Saturday')
        for s6 in t36:
            l6 = s6.third_link
            c6.append(l6)
                # code for 4th lecture of every day

    name3 = student_tymtable.objects.values('fourth_lech_teacher')
    cats3 = {item['fourth_lech_teacher'] for item in name3}
    print(cats)
    p1=[]
    p2=[]
    p3=[]
    p4=[]
    p5=[]
    p6=[]
    for cat in cats3:
        u7 = student_tymtable.objects.filter(fourth_lech_teacher=cat, day='Monday')
        for k in u7:
            p1.append(k.fourth_lech_teacher)
        u8 = student_tymtable.objects.filter(fourth_lech_teacher=cat, day='Tuesday')
        for k2 in u8:
            p2.append(k2.fourth_lech_teacher)
        u9 = student_tymtable.objects.filter(fourth_lech_teacher=cat, day='Wednesday')
        for k3 in u9:
            p3.append(k3.fourth_lech_teacher)
        u10 = student_tymtable.objects.filter(fourth_lech_teacher=cat, day='Thursday')
        for k4 in u10:
            p4.append(k4.fourth_lech_teacher)
        u11 = student_tymtable.objects.filter(fourth_lech_teacher=cat, day='Friday')
        for k5 in u11:
            p5.append(k5.fourth_lech_teacher)
        u12 = student_tymtable.objects.filter(fourth_lech_teacher=cat, day='Saturday')
        for k6 in u12:
            p6.append(k6.fourth_lech_teacher)
    for q in p1:
        t41 = teacher_timetable.objects.filter(name=q, day='Monday')
        print(t1)
        for s1 in t41:
            l1 = s1.fourth_link
            d1.append(l1)
    for q in p2:
        t42 = teacher_timetable.objects.filter(name=q, day='Tuesday')
        for s2 in t42:
            l2 = s2.fourth_link
            d2.append(l2)
    for q in p3:
        t43 = teacher_timetable.objects.filter(name=q, day='Wednesday')
        for s3 in t43:
            l3 = s3.fourth_link
            d3.append(l3)
    for q in p4:
        t43 = teacher_timetable.objects.filter(name=q, day='Thursday')
        for s4 in t43:
            l4 = s4.fourth_link
            d4.append(l4)
    for q in p5:
        t45 = teacher_timetable.objects.filter(name=q, day='Friday')
        for s5 in t45:
            l5 = s5.fourth_link
            d5.append(l5)
    for q in p6:
        t46 = teacher_timetable.objects.filter(name=q, day='Saturday')
        for s6 in t46:
            l6 = s6.fourth_link
            d6.append(l6)

    # code for 5th lecture of every day

    name4 = student_tymtable.objects.values('fifth_lech_teacher')
    cats4 = {item['fifth_lech_teacher'] for item in name4}
    m1=[]
    m2=[]
    m3=[]
    m4=[]
    m5=[]
    m6=[]
    print(cats)
    for cat in cats4:
        v1 = student_tymtable.objects.filter(fifth_lech_teacher=cat, day='Monday')
        for k in v1:
            m1.append(k.fifth_lech_teacher)
        v2 = student_tymtable.objects.filter(fifth_lech_teacher=cat, day='Tuesday')
        for k2 in v2:
            m2.append(k2.fifth_lech_teacher)
        v3 = student_tymtable.objects.filter(fifth_lech_teacher=cat, day='Wednesday')
        for k3 in v3:
            m3.append(k3.fifth_lech_teacher)
        v4 = student_tymtable.objects.filter(fifth_lech_teacher=cat, day='Thursday')
        for k4 in v4:
            m4.append(k4.fifth_lech_teacher)
        v5 = student_tymtable.objects.filter(fifth_lech_teacher=cat, day='Friday')
        for k5 in v5:
            m5.append(k5.fifth_lech_teacher)
        v6 = student_tymtable.objects.filter(fifth_lech_teacher=cat, day='Saturday')
        for k6 in v6:
            m6.append(k6.fifth_lech_teacher)
    for q in m1:
        t51 = teacher_timetable.objects.filter(name=q, day='Monday')
        print(t1)
        for s1 in t51:
            l1 = s1.fifth_link
            e1.append(l1)
    for q in m2:
        t52 = teacher_timetable.objects.filter(name=q, day='Tuesday')
        for s2 in t52:
            l2 = s2.fifth_link
            e2.append(l2)
    for q in m3:
        t53 = teacher_timetable.objects.filter(name=q, day='Wednesday')
        for s3 in t53:
            l3 = s3.fifth_link
            e3.append(l3)
    for q in m4:
        t54 = teacher_timetable.objects.filter(name=q, day='Thursday')
        for s4 in t54:
            l4 = s4.fifth_link
            e4.append(l4)
    for q in m5:
        t55 = teacher_timetable.objects.filter(name=q, day='Friday')
        for s5 in t55:
            l5 = s5.fifth_link
            e5.append(l5)
    for q in m6:
        t56 = teacher_timetable.objects.filter(name=q, day='Saturday')
        for s6 in t56:
            l6 = s6.fifth_link
            e6.append(l6)

            # code for 6th lecture of every day

    name5 = student_tymtable.objects.values('third_lech_teacher')
    cats5 = {item['third_lech_teacher'] for item in name5}
    print(cats)
    m7=[]
    m8=[]
    m9=[]
    m10=[]
    m11=[]
    m12=[]
    for cat in cats5:
        v7 = student_tymtable.objects.filter(sixth_lech_teacher=cat, day='Monday')
        for k in v7:
            m7.append(k.sixth_lech_teacher)
        v8 = student_tymtable.objects.filter(sixth_lech_teacher=cat, day='Tuesday')
        for k2 in v8:
            m8.append(k2.sixth_lech_teacher)
        v9 = student_tymtable.objects.filter(sixth_lech_teacher=cat, day='Wednesday')
        for k3 in v9:
            m9.append(k3.sixth_lech_teacher)
        v10 = student_tymtable.objects.filter(sixth_lech_teacher=cat, day='Thursday')
        for k4 in v10:
            m10.append(k4.sixth_lech_teacher)
        v11 = student_tymtable.objects.filter(sixth_lech_teacher=cat, day='Friday')
        for k5 in v11:
            m11.append(k5.sixth_lech_teacher)
        v12 = student_tymtable.objects.filter(sixth_lech_teacher=cat, day='Saturday')
        for k6 in v12:
            m12.append(k6.sixth_lech_teacher)
    for q in m7:
        t61 = teacher_timetable.objects.filter(name=q, day='Monday')
        print(t1)
        for s1 in t61:
            l1 = s1.sixth_link
            f1.append(l1)
    for q in m8:
        t62 = teacher_timetable.objects.filter(name=q, day='Tuesday')
        for s2 in t62:
            l2 = s2.sixth_link
            f2.append(l2)
    for q in m9:
        t63 = teacher_timetable.objects.filter(name=q, day='Wednesday')
        for s3 in t63:
            l3 = s3.sixth_link
            f3.append(l3)
    for q in m10:
        t64 = teacher_timetable.objects.filter(name=q, day='Thursday')
        for s4 in t64:
            l4 = s4.sixth_link
            f4.append(l4)
    for q in m11:
        t65 = teacher_timetable.objects.filter(name=q, day='Friday')
        for s5 in t65:
            l5 = s5.sixth_link
            f5.append(l5)
    for q in m12:
        t66 = teacher_timetable.objects.filter(name=q, day='Saturday')
        for s6 in t66:
            l6 = s6.sixth_link
            f6.append(l6)
                # code for 7th lecture of every day

    name6 = student_tymtable.objects.values('sev_lech_teacher')
    cats6 = {item['sev_lech_teacher'] for item in name6}
    print(cats)
    p11=[]
    p22=[]
    p33=[]
    p44=[]
    p55=[]
    p66=[]
    for cat in cats3:
        j7 = student_tymtable.objects.filter(sev_lech_teacher=cat, day='Monday')
        for k in j7:
            p11.append(k.sev_lech_teacher)
        j8 = student_tymtable.objects.filter(sev_lech_teacher=cat, day='Tuesday')
        for k2 in j8:
            p22.append(k2.sev_lech_teacher)
        j9 = student_tymtable.objects.filter(sev_lech_teacher=cat, day='Wednesday')
        for k3 in j9:
            p33.append(k3.sev_lech_teacher)
        j10 = student_tymtable.objects.filter(sev_lech_teacher=cat, day='Thursday')
        for k4 in j10:
            p44.append(k4.sev_lech_teacher)
        j11 = student_tymtable.objects.filter(sev_lech_teacher=cat, day='Friday')
        for k5 in j11:
            p55.append(k5.sev_lech_teacher)
        j12 = student_tymtable.objects.filter(sev_lech_teacher=cat, day='Saturday')
        for k6 in j12:
            p66.append(k6.sev_lech_teacher)
    for q in p11:
        t71 = teacher_timetable.objects.filter(name=q, day='Monday')
        print(t1)
        for s1 in t71:
            l1 = s1.seventh_link
            g1.append(l1)
    for q in p22:
        t72 = teacher_timetable.objects.filter(name=q, day='Tuesday')
        for s2 in t72:
            l2 = s2.seventh_link
            g2.append(l2)
    for q in p33:
        t73 = teacher_timetable.objects.filter(name=q, day='Wednesday')
        for s3 in t73:
            l3 = s3.seventh_link
            g3.append(l3)
    for q in p44:
        t73 = teacher_timetable.objects.filter(name=q, day='Thursday')
        for s4 in t73:
            l4 = s4.seventh_link
            g4.append(l4)
    for q in p55:
        t75 = teacher_timetable.objects.filter(name=q, day='Friday')
        for s5 in t75:
            l5 = s5.seventh_link
            g5.append(l5)
    for q in p66:
        t76 = teacher_timetable.objects.filter(name=q, day='Saturday')
        for s6 in t76:
            l6 = s6.seventh_link
            g6.append(l6)

    #print(t1)

    #print(a)
    context = {
        'roll': items[x].rollnumber,
        'course': items[x].specialization,
        'table':table,
        'a1': a1,
        'a2': a2,
        'a3': a3,
        'a4': a4,
        'a5': a5,
        'a6': a6,
        'b1': b1,
        'b2': b2,
        'b3': b3,
        'b4': b4,
        'b5': b5,
        'b6': b6,
        'c1': c1,
        'c2': c2,
        'c3': c3,
        'c4': c4,
        'c5': c5,
        'c6': c6,
        'd1': d1,
        'd2': d2,
        'd3': d3,
        'd4': d4,
        'd5': d5,
        'd6': d6,
        'e1': e1,
        'e2': e2,
        'e3': e3,
        'e4': e4,
        'e5': e5,
        'e6': e6,
        'f1': f1,
        'f2': f2,
        'f3': f3,
        'f4': f4,
        'f5': f5,
        'f6': f6,
        'g1': g1,
        'g2': g2,
        'g3': g3,
        'g4': g4,
        'g5': g5,
        'g6': g6,

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
    django_logout(request)
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
            django_login(request, user)
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
def c_tymtable(request):
    form=teacher_timetableform()
    if request.method=='POST':
        form=teacher_timetableform(request.POST)
        if form.is_valid:
            form.save()
            return HttpResponseRedirect(reverse('tymtable'))
    context={'form':form}
    return render(request,'accounts/about.html',context)