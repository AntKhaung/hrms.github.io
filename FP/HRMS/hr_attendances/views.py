from django.shortcuts import render, redirect
from .models import AttendanceModel
from .forms import AttendanceForm
from datetime import datetime
from django.db.models import Q
from django.contrib.auth.decorators import login_required, permission_required
# Create your views here.


def search_by(request):
    search = request.GET.get('search')
    if search:
        attendances = AttendanceModel.objects.filter(
            Q(name__icontains=search) |
            Q(check_in__icontains=search) |
            Q(check_out__icontains=search) |
            Q(date__icontains=search)
        )
    else:
        attendances = AttendanceModel.objects.all()
    return render(request, 'attendance_list.html', {'all_attendances': attendances})

@login_required(login_url='login')
def attendance(request, attendance_id):
	if request.method == "GET":
		attendance = AttendanceModel.objects.get(id=attendance_id)
		return render(request,'attendance_datail.html', {'attendance': attendance})

@login_required(login_url='login')
def all_attendances(request):
	 if request.method == "GET":
	 	all_attendances = AttendanceModel.objects.all()
	 return render(request,'attendance_list.html', {'all_attendances': all_attendances})

@permission_required('hr_attendances.add_attendancemodel', login_url='login')
def add_attendance(request):
	if request.method == "GET":
		form = AttendanceForm()
		return render(request,'attendance_create.html',{'form':form})
	if request.method == "POST":
		form = AttendanceForm(request.POST)
		if form.is_valid():
			name = form.cleaned_data.get('name')
			check_in = form.cleaned_data.get('check_in')
			check_out = form.cleaned_data.get('check_out')
			date = form.cleaned_data.get('date')
			description = form.cleaned_data.get('description')
			attendance = AttendanceModel.objects.create(
				name=name,
				check_in=check_in,
				check_out=check_out,
				date=date,
				description=description,
			)
			attendance.save()
			return redirect('/hr_attendances/show_attendance/')

@permission_required('hr_attendances.change_attendancemodel', login_url='login')
def update_attendance(request, attendance_id):
	attendance = AttendanceModel.objects.get(id=attendance_id)
	if request.method == "GET":
		values = {
			'name': attendance.name,
			'check_in': attendance.check_in,
			'check_out': attendance.check_out,
			'date': attendance.date,
			'description': attendance.description,
		}
		form = AttendanceForm(initial=values)
		context = {'form': form, 'attendance': attendance}
		return render(request, 'attendance_update.html', context)
	elif request.method == "POST":
		form = AttendanceForm(request.POST)
		if form.is_valid():
			attendance.name = form.cleaned_data.get('name')
			attendance.check_in = form.cleaned_data.get('check_in')
			attendance.check_out = form.cleaned_data.get('check_out')
			attendance.date = form.cleaned_data.get('date')
			attendance.description = form.cleaned_data.get('description')
			attendance.save()
			return redirect('/hr_attendances/detail/' + str(attendance_id) + '/')

@permission_required('hr_attendances.delete_attendancemodel', login_url='login')
def delete_attendance(request, attendance_id):
	if request.method == "GET":
		attendance = AttendanceModel.objects.get(id=attendance_id)
		attendance.delete()
		return redirect('/hr_attendances/show_attendance/')
