from django.contrib import admin
from django.urls import path
from jobseeker import views
urlpatterns = [
    path("", views.index, name='home'),
    path("contact", views.contact, name='contact'),
    path("Jobform", views.Jobform, name='Jobform'),
    path('contactinfo/', views.contactinfo, name="contactinfo"),
    path('jobforminfo/', views.jobforminfo, name="jobforminfo"),
    path('MyWebsite/', views.MyWebsite, name="MyWebsite"),
    path('AboutUs/', views.AboutUs, name="AboutUs"),
    path('SignIn/', views.SignIn, name="SignIn"),
    path('Signin_info/', views.Signin_info, name="Signin_info"),
]