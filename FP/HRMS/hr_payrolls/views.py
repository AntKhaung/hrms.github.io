from django.shortcuts import render, redirect
from .models import PayrollModel
from .forms import PayrollForm
from django.db.models import Q
# Create your views here.

def search_by(request):
    search = request.GET.get('search')
    if search:
        payroll = PaurollModel.objects.filter(
            Q(name__icontains=search) |
            Q(ammount__icontains=search) |
            Q(note__icontains=search) |
            Q(status__icontains=search) |
            Q(date__icontains=search)
        )
    else:
        payrolls = PayrollModel.objects.all()
    return render(request, 'payroll_list.html', {'all_payrolls': payrolls})

def order_by(request):
    order = request.GET.get('order')
    payrolls = PayrollModel.objects.all().order_by("-"+ order)
    order_selected = {str(order)}
    context = {'all_payrolls': payrolls, 'order_selected': order_selected}
    return render(request, 'payroll_list.html', context)

def payroll(request, payroll_id):
	if request.method == "GET":
		payroll = PayrollModel.objects.get(id=payroll_id)
		form = PayrollForm(instance=payroll)
		return render(request,'payroll_detail.html', {'form': form, 'payroll': payroll})

def all_payrolls(request):
	if request.method == "GET":
		all_payrolls = PayrollModel.objects.all()
		context = {'all_payrolls': all_payrolls}
		return render(request,'payroll_list.html', context)

def add_payroll(request):
	if request.method == "GET":
		form = PayrollForm()
		return render(request,'payroll_create.html',{'form':form})
	if request.method == "POST" and request.FILES['attachment']:
		form = PayrollForm(request.POST, request.FILES)
		if form.is_valid():
			form.save()
			return redirect('/hr_payrolls/show_payroll/')

def update_payroll(request,	payroll_id):
	payroll = PayrollModel.objects.get(id=payroll_id)
	if request.method == "GET":
		form = PayrollForm(instance=payroll)
		return render(request, 'payroll_update.html', {'form': form})
	elif request.method == "POST":
		form = PayrollForm(request.POST, request.FILES, instance=payroll)
		if form.is_valid():
			form.save()
			return redirect('/hr_payrolls/detail/' + str(payroll_id) + '/')

# @permission_required('hr_jobs.delete_jobmodel', login_url='login')
def delete_payroll(request, payroll_id):
	if request.method == "GET":
		payroll = PayrollModel.objects.get(id=payroll_id)
		payroll.delete()
		return redirect('/hr_payrolls/show_payroll/')