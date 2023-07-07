from django.shortcuts import render, redirect

# Create your views here.
from .models import JobModel
from .forms import JobForm
from django.contrib.auth.decorators import login_required, permission_required

from django.db.models import Q

def search_by(request):
    print('search_by call')
    search = request.GET.get('search')
    if search:
        jobs = JobModel.objects.filter(
            Q(name__icontains=search) |
            Q(open_date__icontains=search) |
            Q(note__icontains=search) |
            Q(status__icontains=search) |
            Q(create_date__icontains=search)
        )
    else:
        jobs = JobModel.objects.all()
    return render(request, 'job_list.html', {'all_jobs': jobs})

def order_by(request):
    print('order_by call')
    order = request.GET.get('order')
    jobs = JobModel.objects.all().order_by("-"+ order)
    order_selected = {str(order): 'btn-primary text-white'}
    context = {'all_jobs': jobs, 'order_selected': order_selected}
    return render(request, 'job_list.html', context)

@permission_required('hr_jobs.view_jobmodel', login_url='login')
def job(request, job_id):
	if request.method == "GET":
		job = JobModel.objects.get(id=job_id)
		form = JobForm(instance=job)
		return render(request,'job_detail.html', {'form': form, 'job': job})

@login_required(login_url='login')
def all_jobs(request):
	print('all_jobs call')
	if request.method == "GET":
		print('all_jobs GET call')
		all_jobs = JobModel.objects.all()
		# SELECT * FROM Jobs;
		context = {'all_jobs': all_jobs}
		return render(request,'job_list.html', context)

@permission_required('hr_jobs.add_jobmodel', login_url='login')
def add_job(request):
	print('add_job call')
	if request.method == "GET":
		print('add_job GET call')
		form = JobForm()
		return render(request,'job_create.html',{'form':form})
	if request.method == "POST" and request.FILES['attachment']:
		print('add_job POST call')
		print('data => ', request.POST)
		form = JobForm(request.POST, request.FILES)
		if form.is_valid():
			print('form is valid')
			form.save()
			return redirect('/hr_jobs/show_job/')

@permission_required('hr_jobs.change_jobmodel', login_url='login')
def update_job(request, job_id):
	print('update_job call')
	print('job_id ', job_id)
	job = JobModel.objects.get(id=job_id)
	if request.method == "GET":
		print('update_job GET call')
		form = JobForm(instance=job)
		return render(request, 'job_update.html', {'form': form, 'uploaded_image': job.attachment})
	elif request.method == "POST":
		print('update_job POST call')
		print('data => ', request.POST)
		form = JobForm(request.POST, request.FILES, instance=job)
		if form.is_valid():
			print('form is valid')
			form.save()
			return redirect('/hr_jobs/detail/' + str(job_id) + '/')

@permission_required('hr_jobs.delete_jobmodel', login_url='login')
def delete_job(request, job_id):
	if request.method == "GET":
		job = JobModel.objects.get(id=job_id)
	# 	return render(request, 'job_delete.html', {'job': job})
	# if request.method == "POST":
	# 	job = JobModel.objects.filter(id=job_id)
		job.delete()
		return redirect('/hr_jobs/show_job/')