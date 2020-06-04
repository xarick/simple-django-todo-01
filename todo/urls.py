from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.TodoIndex, name='index'),
    path('login/', views.TodoLogin, name='login'),
    path('logout/', views.TodoLogout, name='logout'),
    re_path(r'^delete/(?P<student_id>\d+)/$', views.TodoDelete, name='delete'),
    re_path(r'^update/(?P<student_id>\d+)/$', views.TodoUpdate, name='update'),
]