from django.urls import path

from . import views

app_name='mapevent'

urlpatterns = [
	path('', views.index, name='index'),
]
