from django.shortcuts import render,redirect,reverse
from .forms import *
from django.contrib.auth.decorators import login_required
from django.db.models import Sum
from django.contrib import messages
# Create your views here.

@login_required
def index(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            form = form.save(commit=False)
            form.user = request.user
            form.save()
            return redirect(reverse('demoapp:dashboard'))
        else:
            args = {'form': form}
            print(form.errors)
            return render(request, 'demoapp/index.html', args)
    else:
        form = ExpenseForm()
        args = {'form': form}
        return render(request, 'demoapp/index.html', args)

@login_required
def dashboard(request):
    expenses = Expense.objects.all()
    expenses_per_person= Expense.objects.values('user').annotate(Sum('expense_amount'))
    print(expenses_per_person)
    context={'expenses':expenses,'expenses_per_person':expenses_per_person}
    return render(request,'demoapp/dashboard.html',context=context)


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'user created successfully')
            return redirect(reverse('login'))
        else:
            args = {'form': form}
            return render(request, 'demoapp/register.html', args)
    else:
        form = RegistrationForm()
        args = {'form': form}
        return render(request, 'demoapp/register.html', args)




