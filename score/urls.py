
from django.urls import path, re_path
from . import views

app_name='score'

urlpatterns = [
    path('', views.login, name='login'),
    path('login', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('upload/', views.upload, name='upload'),
    path('show', views.show, name='show'),

]
