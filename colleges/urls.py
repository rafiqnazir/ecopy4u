from django.urls import path
from . import views
from .views import CollegeList,BranchList,PaperList,CollegePaperCreate

urlpatterns = [
    path('',CollegeList.as_view(),name='colleges'),
    path('<str:college_name>/branch/',BranchList.as_view(),name='branches'),
    path('<str:college_name>/<str:branch>/paper/',PaperList.as_view(),name='college-papers'),
    path('new/',CollegePaperCreate.as_view(),name='college-paper-create'),
]
