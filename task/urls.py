from django.conf.urls import url

from . import views

urlpatterns = [
	url(r'^time/', views.time, name='time')
]