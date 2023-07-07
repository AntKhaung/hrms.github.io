from django.shortcuts import render, redirect
from .models import ExpenseModel
from .forms	import ExpenseForm
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.

def search_by(request):
    search = request.GET.get('search')
    if search:
        expenses = ExpenseModel.objects.filter(
            Q(description__icontains=search) |
            Q(product__icontains=search) |
            Q(expense_date__icontains=search) |
            Q(note__icontains=search) |
            Q(total_ammount__icontains=search) |
            Q(paid_by__icontains=search)
        )
    else:
        expenses = ExpensesModel.objects.all()
    return render(request, 'expense_list.html', {'all_expenses': expenses})

def order_by(request):
    order = request.GET.get('order')
    expenses = ExpenseModel.objects.all().order_by("-"+ order)
    context = {'all_expenses': expenses}
    return render(request, 'expense_list.html', context)

@login_required(login_url='login')
def expense(request, expense_id):
	if request.method == "GET":
		expense = ExpenseModel.objects.get(id=expense_id)
		form = ExpenseForm(instance=expense)
		return render(request,'expense_detail.html', {'form': form, 'expense': expense})

@login_required(login_url='login')
def all_expenses(request):
	if request.method == "GET":
		all_expenses = ExpenseModel.objects.all()
		return render(request,'expense_list.html', {'all_expenses': all_expenses})

def add_expense(request):
	if request.method == "GET":
		form = ExpenseForm()
		return render(request,'expense_create.html',{'form':form})
	if request.method == "POST" and request.FILES['attachment']:
		form = ExpenseForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/hr_expenses/show_expense/')

@permission_required('hr_expenses.change_expensemodel', login_url='login')
def update_expense(request, expense_id):
	expense = ExpenseModel.objects.get(id=expense_id)
	if request.method == "GET":
		form = ExpenseForm(instance=expense)
		return render(request, 'expense_update.html', {'form': form})
	elif request.method == "POST":
		form = ExpenseForm(request.POST, request.FILES, instance=expense)
		if form.is_valid():
			form.save()
			return redirect('/hr_expenses/detail/' + str(expense_id) + '/')

@permission_required('hr_expenses.delete_expensemodel', login_url='login')
def delete_expense(request, expense_id):
	if request.method == "GET":
		expense = ExpenseModel.objects.get(id=expense_id)
		expense.delete()
		return redirect('/hr_expenses/show_expense/')