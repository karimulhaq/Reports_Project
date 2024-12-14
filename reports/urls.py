
from django.urls import path
from django.http import HttpResponse
from . import views

app_name = 'reports'
urlpatterns = [
    path('', views.home , name='home'),
    path('newreport/', views.new_report, name='new_report'),
    path('update/<int:pk>', views.update_report, name='update_report'),
    path('delete/<int:pk>', views.delete_report, name='delete_report'),
    path('about/', views.aboutme, name='about'),
]


