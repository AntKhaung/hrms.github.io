from django.shortcuts import render, redirect

# Create your views here.
from django.views.generic import ListView, CreateView, DeleteView, UpdateView, DetailView
from django.urls import reverse_lazy
from hr_recruitments import models
from hr_recruitments import forms
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from django.db.models import Q
from django.views import View
from .models import ResumeModel

class SearchBy(View):

    def get(self, request):
        search = request.GET.get('search')
        if search:    
            resumes = ResumeModel.objects.filter(
                Q(name__icontains=search) | 
                Q(sequence__icontains=search) |
                Q(appointment_date__icontains=search) |
                Q(note__icontains=search) |
                Q(status__icontains=search) |
                Q(create_date__icontains=search)
            )
        else:      
            resuems = ResumeModel.objects.all()
        return render(request, 'resume_list.html', {'all_resumes': resumes})

class OrderBy(View):

    def get(self, request):
        order = request.GET.get('order')
        resumes = ResumeModel.objects.all().order_by("-"+ order)
        order_selected = {str(order): 'btn-primary text-white'}
        return render(request, 'resume_list.html', {'all_resumes': resumes, 'order_selected': order_selected})

class ResumeListView(LoginRequiredMixin, ListView):
	login_url = 'login'
	model = models.ResumeModel
	context_object_name = 'all_resumes'
	template_name = 'resume_list.html'

class ResumeCreateView(PermissionRequiredMixin, CreateView):
	permission_required = 'hr_recruitments.add_resumemodel'
	login_url = 'login'
	success_url = reverse_lazy("resume_list")
	model = models.ResumeModel
	form_class = forms.ResumeForm
	template_name = 'resume_create.html'

class ResumeUpdateView(PermissionRequiredMixin, UpdateView):
	permission_required = 'hr_recruitments.change_resumemodel'
	login_url = 'login'
	success_url = reverse_lazy("resume_list")
	model = models.ResumeModel
	form_class = forms.ResumeForm
	context_object_name = "resume"
	template_name = 'resume_update.html'

class ResumeDetailView(PermissionRequiredMixin, DetailView):
	permission_required = 'hr_recruitments.view_resumemodel'
	login_url = 'login'
	model = models.ResumeModel
	form_class = forms.ResumeForm
	context_object_name = "resume"
	template_name = 'resume_detail.html'

	# def get_context_data(self, **kwargs):
	# 	context = super(ResumeDetailView, self).get_context_data(**kwargs)
	# 	resume = models.ResumeModel.objects.get(id=self.kwargs.get('pk'))
	# 	form = forms.ResumeForm(instance=resume)
	# 	context['form'] = form
	# 	return context

class ResumeDeleteView(PermissionRequiredMixin, DeleteView):
	permission_required = 'hr_recruitments.delete_resumemodel'
	login_url = 'login'
	# success_url = reverse_lazy("resume_list")
	# model = models.ResumeModel
	# context_object_name = "resume"
	# template_name = 'resume_delete.html'

	def get(self, request, pk):
		resume = models.ResumeModel.objects.get(id=pk)  
		resume.delete()
		return redirect('resume_list')