from django.urls import path
from hr_attendances import views

urlpatterns = [
	path('show_attendance/', views.all_attendances),
	path('new_attendance/', views.add_attendance),
	path('detail/<int:attendance_id>/', views.attendance),
	path('update/<int:attendance_id>/', views.update_attendance),
	path('delete/<int:attendance_id>/', views.delete_attendance),
	path('search_by/', views.search_by),
]