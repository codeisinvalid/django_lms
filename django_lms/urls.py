
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('base/', views.BASE, name='base'),
    path('', views.home, name='home'), 
    path('single_course/', views.single_course, name= 'singlecourse'),
]
