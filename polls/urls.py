from django.urls import path
from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^hello/', views.hello_world, name='hello')
]
