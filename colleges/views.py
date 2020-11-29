from django.shortcuts import render,get_object_or_404
from colleges.models import colleges
from django.views.generic import ListView, DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
from home.models import views
from django.shortcuts import redirect
from django.db import IntegrityError

class CollegeList(ListView):
	Views=views.objects.first()
	Views.colleges += 1
	Views.save()
	model = colleges
	template_name = "colleges/colleges.html"
	context_object_name = "colleges"
	allow_empty=False
	# No of Contents/rows per page
	paginate_by=20
	def get_queryset(self):
		return colleges.objects.values('college_name').filter(valid=True).distinct().order_by('college_name')

class BranchList(ListView):
	model = colleges
	template_name = "colleges/branches.html"
	allow_empty=False
	context_object_name = "colleges"
	# No of Contents/rows per page
	paginate_by=20

	def get_queryset(self):
		college=self.kwargs.get('college_name')
		return colleges.objects.filter(college_name=college,valid=True).values('branch','college_name').distinct().order_by('branch')
class PaperList(ListView):
	Views=views.objects.first()
	Views.downloads += 1
	Views.save()
	model = colleges
	template_name = "colleges/papers.html"
	allow_empty=False
	context_object_name = "colleges"
	# No of Contents/rows per page
	paginate_by=20
	def get_queryset(self):
		Branch=self.kwargs.get('branch')
		college=self.kwargs.get('college_name')
		return colleges.objects.filter(college_name=college,branch=Branch,valid=True).order_by('subject','-year')

class CollegePaperCreate(LoginRequiredMixin,SuccessMessageMixin,CreateView):
	model=colleges
	fields = ['college_name','branch','subject','year','exam','pdf']
	def post(self, request, *args, **kwargs):
		# super().post() maybe raise a ValidationError if it is failure to save
		response = super().post(request, *args, **kwargs)
		if not self.object:
			messages.info(request,'This Paper Already Exists. Contact us for any problem')
		else:
			messages.info(request,'Thanks, your paper will be uploaded after validation.')
		return response

	def form_valid(self,form):
	    form.instance.contributor= self.request.user
	    # messages.success(request,f'Congratulations!!! Your paper has been added')
	    try:
	    	return super().form_valid(form)
	    except IntegrityError:
	    	return redirect('college-paper-create')