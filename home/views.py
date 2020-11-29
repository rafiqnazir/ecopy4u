from django.shortcuts import render
from boards.models import boards
from colleges.models import colleges
from .models import views
# Create your views here.

def main(request):
	Views=views.objects.first()
	if(request.user.is_authenticated and request.user.username=='rafiq'):
		Views.save()
	else:
		Views.home+=1
		Views.save()
	context={
	'total':boards.objects.count()+colleges.objects.count(),
	'views':Views.home + Views.boards + Views.colleges+Views.downloads
	}
	return render(request,'home/home.html',context)

