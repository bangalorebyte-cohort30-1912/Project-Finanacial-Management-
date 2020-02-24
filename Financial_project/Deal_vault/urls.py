from django.urls import path
from django.views.generic.base import TemplateView
from .views import get_info , uilogout
from . import views

urlpatterns = [
    # path('signup/', views.SignUp.as_view(), name='Signup'),
	path('',get_info,name='get_info'),
    path('logout',uilogout, name='logout')
]