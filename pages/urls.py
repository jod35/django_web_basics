from django.urls import path
from . import views

urlpatterns = [
    path('',views.HomePage.as_view(),name='pages_home'),
    path('about/',views.AboutPage.as_view(),name='pages_about')
]