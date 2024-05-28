from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomeView.as_view(), name="home"),
    path('create-poem', views.CreatePoem.as_view(), name='create-poem')
]


#CRUD
#create
#read
#update
#delete