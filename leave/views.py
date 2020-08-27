from django.shortcuts import render,redirect
from .forms import ApplyForm, CreateUserForm,ApplyForm1, EmployeeForm, CommentForm
from .models import *
from django.contrib.auth.forms import UserCreationForm
from .filters import LeaveFilter
from datetime import datetime, timedelta
from datetime import date
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users, head_only
from django.contrib.auth.models import Group


from django.contrib import messages

# Create your views here.
@unauthenticated_user
def registerpage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='employee')
            user.groups.add(group)
            Created_emp = employee.objects.create(
                user =user,
                
            )
            L1 = leave.objects.get(name="Sick Leaves")
            L2 = leave.objects.get(name="Annual Leaves")
            L3 = leave.objects.get(name="Casual Leaves")
            L4 = leave.objects.get(name="Short Leaves")
            Created_emp.leave.add(L1,L2,L3,L4)
            Created_emp.save()

            messages.success(request, 'Account was created for '+username)
            return redirect('login')

    context= {'form':form}
    return render(request, 'home/register.html',context)

@unauthenticated_user
def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('leaves')
        else:
            messages.info(request, 'Username OR Password is incorrect')
                
    context = {}
    return render(request, 'home/login.html',context)

def logoutUser(request):
    logout(request)
    return redirect('login')

def home(request):
    form = CommentForm()
    if request.method == "GET":
        form = CommentForm()
        return render(request, 'home/homepage.html', {'form':form})

    else:
        form = CommentForm(request.POST)
        if form.is_valid():
            form.save()
        messages.success(request, 'Your Comment has been sent successfully. You will have reply soon')
        return redirect('home-page')
        

@login_required(login_url='login')
@allowed_users(allowed_roles=['employee'])
def accountSettings(request):
    employee = request.user.employee
    form = EmployeeForm(instance=employee)

    if request.method == 'POST':
        form = EmployeeForm(request.POST, request.FILES, instance=employee)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your Profile has been updated successfully')


    context = {'form':form}
    return render(request, 'home/Profile.html',context)


def head(request):
    return render(request, 'home/head.html')

def res_leaves(request):
    leaves = apply.objects.filter(employee__department=request.user.head.department)

    respondedLeave = leaves.exclude(status='Pending').order_by('-date_created')
    

    context = {'leaves':leaves,'respondedLeave':respondedLeave}
    return render(request, 'home/Res_leaves.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['head'])
def employee1(request, pk_test):
    employee1 = employee.objects.get(id=pk_test)
    applys = employee1.apply_set.all().order_by('-date_created')

    allleaves = employee1.leave.all()
    allleaves1 = apply.objects.all().filter(employee=employee1)
    approved_leaves = allleaves1.filter(status='Approved')
    leave_type = leave.objects.all()

    leaveData = {}
    leaveData1 = {}

    for Newleave in leave_type:
        leaveobject =  approved_leaves.filter(leave__name=Newleave.name)
        total_leave = 0
        for leaveInstance in leaveobject:
            Datediff = leaveInstance.to_date - leaveInstance.from_date
            Real = Datediff.days + 1
            total_leave = total_leave + Real
            ava = leaveInstance.leave.Number_of_Leaves - total_leave
        leaveData[Newleave.name]=total_leave

    apply_count = applys.count()
    myFilter = LeaveFilter(request.GET, queryset=applys)
    applys = myFilter.qs

    context ={'employee1':employee1, 'applys':applys, 'apply_count':apply_count,
    'allleaves':allleaves,'myFilter':myFilter,'usedLeave':leaveData}
    #context = {**context, **leaveData}

    return render(request, 'home/employee.html',context)

@login_required(login_url='login')
@allowed_users(allowed_roles=['employee'])
def user_page(request):
    applys = request.user.employee.apply_set.all().order_by('-date_created')
    allleaves = request.user.employee.leave.all()
    myFilter = LeaveFilter(request.GET, queryset=applys)
    applys = myFilter.qs

    allleaves1 = apply.objects.all().filter(employee=request.user.employee)
    approved_leaves = allleaves1.filter(status='Approved')
    leave_type = leave.objects.all()

    leaveData = {}
    leaveData1 = {}

    for Newleave in leave_type:
        leaveobject =  approved_leaves.filter(leave__name=Newleave.name)
        total_leave = 0
        for leaveInstance in leaveobject:
            Datediff = leaveInstance.to_date - leaveInstance.from_date
            Real = Datediff.days + 1
            total_leave = total_leave + Real
        leaveData[Newleave.name]=total_leave

        
    context = {'applys':applys,'allleaves':allleaves,'myFilter':myFilter,'usedLeave':leaveData}
    return render(request, 'home/user.html',context)

@login_required(login_url='login')
@head_only
def leaves(request):
    leaves = apply.objects.filter(employee__department=request.user.head.department)
    
    total_leaves = leaves.count()
    pending = leaves.filter(status='Pending').count
    approved = leaves.filter(status='Approved').count
    rejected = leaves.filter(status='Rejected').count
    pendingLeave = leaves.filter(status='Pending').order_by('-date_created')
    respondedLeave = leaves.exclude(status='Pending').order_by('-date_created')
 
    context = {'leaves':leaves,'total_leaves':total_leaves,'approved':approved,'rejected':rejected, 'pending':pending, 'pendingLeave':pendingLeave, 'respondedLeave':respondedLeave}
    return render(request, "home/leaves.html",context)

@login_required(login_url='login')
@head_only
def updateStatus(request,pk):
    order = apply.objects.get(id=pk)
    form = ApplyForm(instance=order)

    if request.method == 'POST':
        form = ApplyForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/leaves')
    context = {'form':form}
    return render(request, 'home/update_apply.html', context)


@login_required(login_url='login')
@allowed_users(allowed_roles=['employee'])
def apply2(request,pk):
    employee1= User.objects.get(id = pk)
    
    if request.method == "GET":
        form = ApplyForm1(initial={'employee':employee1.employee})
        return render(request, 'home/apply1.html', {'form':form})
    else:
        form = ApplyForm1(request.POST)
        if form.is_valid():
            form.save()
        return redirect('user-page')
      

   


