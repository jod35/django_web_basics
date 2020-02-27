from django.urls import path
from . import views

urlpatterns=[
  path('about/',views.about,name='blog_about'), 
  path('',views.index,name='blog_home')
]