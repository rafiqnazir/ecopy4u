from django.urls import path
from . import views
from .views import BoardList,ClassList,BoardPaperCreate,PaperList

urlpatterns = [
    path('',BoardList.as_view(),name='boards'),
    path('<str:board_name>/class/',ClassList.as_view(),name='classes'),
    path('<str:board_name>/<int:class_number>/paper/',PaperList.as_view(),name='board-papers'),
    path('new/',BoardPaperCreate.as_view(),name='board-paper-create'),
]