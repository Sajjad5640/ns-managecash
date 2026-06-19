from django.shortcuts import render,redirect
from django.contrib.auth import login , logout
from django.contrib.auth.decorators import login_required
from ManageCash.forms import *
from ManageCash.models import *
from django.contrib import messages
from django.views.decorators.cache import never_cache
from django.db.models import Sum


# Create your views here.
def register_page(request):

    if request.method == "POST":
        form_data = RegistrationForm(request.POST)
        if form_data.is_valid():
            form_data.save()
            messages.success(request,"Registration Successful !")
            return redirect(login_page)
        else:
            messages.error(request,"You are making mistake")

    form_data = RegistrationForm()
    context = {
        'page_title' : 'Registration Page',
        'form_data' : form_data,
        'form_title' : 'Registration Form',
        'form_btn' : 'Register'

    }

    return render (request,'master/base-form.html', context)

def login_page (request):
    if request.method == "POST":
        form_data = LoginForm(request,request.POST)
        if form_data.is_valid():
            user = form_data.get_user()
            login(request,user)
            messages.success(request,"Login Successful !")
            return redirect('dashboard_page')


    form_data = LoginForm()
    context = {
        'page_title' : 'Login Page',
        'form_data' : form_data,
        'form_title' : 'Login Form',
        'form_btn' : 'Login'

    }

    return render(request,'master/base-form.html', context)
@login_required
@never_cache
def logout_page (request):
    logout(request)
    messages.success(request,'Logout Successfully')
    return redirect('login_page')
@login_required
@never_cache
def dashboard_page(request):
    current_user = request.user
    total_expense = ExpenseModel.objects.filter(user= current_user).aggregate(
        total = Sum('amount')
    )['total'] or 0

    total_cash =AddCashModel.objects.filter(user = current_user).aggregate(
        total = Sum('amount')
    )['total'] or 0
    current_balance = total_cash - total_expense
    context = {
        'total_cash': total_cash,
        'total_expense' : total_expense,
        'current_balance' : current_balance,

    }


    return render(request,'dashboard.html',context)


@login_required
@never_cache
def cash_list(request):
    cash_data = AddCashModel.objects.filter(user= request.user)
    context = {
        'cash_data' : cash_data,
    }
    return render (request,'cash.html',context)
@login_required
@never_cache
def addcash_page(request):
    current_user = request.user
    if request.method == "POST":
        form_data = AddCashForm(request.POST)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.user = current_user
            data.save()
            messages.success(request,'Successful!!')
            return redirect('cash_list')


    form_data = AddCashForm()
    context = {
        'form_data' : form_data,
        'form_title' :'Add Cash',
        'form_btn' : 'Add',
    }
    return render(request,'master/base-form.html',context)

@login_required
@never_cache
def updatecash_page(request,id):

    curren_user = request.user
    try:
        cash_data = AddCashModel.objects.get(id = id)
    except AddCashForm.DoesNotExist:
        cash_data = None
    if request.method =="POST":
        form_data = AddCashForm(request.POST, instance=cash_data)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.user = curren_user
            data.save()
            messages.success(request,'Update Successful!!')
            return redirect('cash_list')

    form_data = AddCashForm(instance=cash_data)
    context = {
        'form_data':form_data,
        'form_title':"Update Cash",
        'form_btn': "Update",
    }
    return render (request,'master/base-form.html',context)
@login_required
@never_cache
def delete_cash(request,id):
    AddCashModel.objects.get(id=id).delete()
    messages.success(request,"Cash Deleted Successfully!!")
    return redirect ("cash_list")

def expense_list(request):
    expense_data = ExpenseModel.objects.filter(user = request.user)
    context ={
        'expense_data' : expense_data
    }
    return render (request,'expense.html',context)
@login_required
@never_cache
def addexpense_page(request):
    current_user = request.user
    if request.method == "POST":
        form_data = ExpenseForm(request.POST)
        if form_data.is_valid():
            data = form_data.save(commit=False)
            data.user = current_user
            data.save()
            messages.success(request,'Add Successful!!')
            return redirect('cash_list')


    form_data = ExpenseForm()
    context = {
        'form_data' : form_data,
        'form_title' :'Add Expense Data',
        'form_btn' : 'Add',
    }
    return render(request,'master/base-form.html',context)
@login_required

def updateexpnese_page(request,id):
    current_user=request.user
    try:
        expense_data=ExpenseModel.objects.get(id=id)
    except ExpenseModel.DoesNotExist:
        expense_data=None
    if request.method=="POST":
        form_data=ExpenseForm(request.POST,instance=expense_data)
        if form_data.is_valid(): 
            data=form_data.save(commit=False)
            data.user=current_user
            data.save()
            messages.success(request,'Update Cash Successfully')
            return redirect('expense_list')
    form_data=ExpenseForm(instance=expense_data)
    context={
       'form_data':form_data,
       'form_title':'Update Expense Data ',
       'form_btn':'Update'
    }
    
    return render(request,'master/base-form.html',context)
@login_required
@never_cache
def delete_expense(request,id):
    ExpenseModel.objects.get(id=id).delete()
    messages.success(request,'Delete Expense Successfully')
    return redirect('expense_list')