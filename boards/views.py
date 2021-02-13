from django.shortcuts import render,get_object_or_404
from boards.models import boards
from django.views.generic import ListView, DetailView,CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.messages.views import SuccessMessageMixin
# from home.models import views
from django.shortcuts import redirect
from django.db import IntegrityError

class BoardList(ListView):
	# Views=views.objects.first()
	# Views.boards += 1
	# Views.save()
	model = boards
	template_name = "boards/boards.html"
	context_object_name = "boards"
	allow_empty=False
	#ordering=['board_name','class_number','subject','-year','series']
	# No of Contents/rows per page
	paginate_by=20
	def get_queryset(self):
		return boards.objects.values('board_name').filter(valid=True).distinct().order_by('board_name')


class ClassList(ListView):
	model = boards
	template_name = "boards/classes.html"
	allow_empty=False
	context_object_name = "boards"
	# No of Contents/rows per page
	paginate_by=20

	def get_queryset(self):
		board=self.kwargs.get('board_name')
		return boards.objects.filter(board_name=board,valid=True).values('class_number','board_name').distinct().order_by('class_number')

class PaperList(ListView):
	# Views=views.objects.first()
	# Views.downloads += 1
	# Views.save()
	model = boards
	template_name = "boards/papers.html"
	allow_empty=False
	context_object_name = "boards"
	# No of Contents/rows per page
	paginate_by=20
	def get_queryset(self):
		Class=self.kwargs.get('class_number')
		board=self.kwargs.get('board_name')
		return boards.objects.filter(board_name=board,class_number=Class,valid=True).order_by('subject','-year')

	
class BoardPaperCreate(SuccessMessageMixin,CreateView):
	model=boards
	fields = ['board_name','class_number','subject','year','series','pdf']

	def post(self, request, *args, **kwargs):
		# super().post() maybe raise a ValidationError if it is failure to save
		response = super().post(request, *args, **kwargs)
		if not self.object:
			messages.info(request,'This Paper Already Exists. Contact us for any problem')
		else:
			messages.info(request,'Thanks, your paper will be uploaded after validation.')
		return response

	def form_valid(self,form):
		if (self.request.user.is_authenticated):
			form.instance.contributor= self.request.user
		# messages.success(request,f'Congratulations!!! Your paper has been added')
		try:
			return super().form_valid(form)
		except IntegrityError:
			return redirect('college-paper-create')
   







   