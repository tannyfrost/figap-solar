from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('test/', views.secondpage, name ='test'),
    path('about/', views.about, name = 'about'),
    path('service/', views.service, name = 'service'),
    path('project/', views.project, name = 'project'),
    path('contact/', views.contact, name = 'contact'),
]
