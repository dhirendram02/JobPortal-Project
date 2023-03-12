from django.shortcuts import render, HttpResponse
from datetime import datetime
from django.contrib.auth.decorators import login_required
from jobseeker.models import JobForm
from .models import Contact
from .models import signin
from django.contrib import messages
# Create your views here.
def index(request):
    context = {
        "variable":"this is sent"
    }
    return render(request, 'index.html', context)

@login_required
def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        Email = request.POST.get('Email')
        phone = request.POST.get('phone')
        desc= request.POST.get('desc')
        contact = Contact(name=name, Email=Email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Your Message Has Been Sent.')
    return render(request, 'contact.html')

@login_required
def Jobform(request):
    if request.method == "POST":
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        Email = request.POST.get('Email')
        phone = request.POST.get('phone')
        JobType= request.POST.get('JobType')
        JobRole= request.POST.get('JobRole')
        Location= request.POST.get('Location')
        Jobform = JobForm(name=name, gender=gender, Email=Email,  phone=phone, JobType=JobType, JobRole=JobRole, Location=Location, date=datetime.today())
        Jobform.save()
        messages.success(request, 'Your Message Has Been Sent.')
    return render(request, 'jobapp.html')

def MyWebsite(request):
    context = {
        "variable1":"Profile is Open"
    }
    return render(request, 'mywebsite.html', context)

def AboutUs(request):
    context = {
        "variable2":"About Us is Open"
    }
    return render(request, 'aboutus.html', context)

def SignIn(request):
    if request.method=="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        SignIn = signin(username=username, password=password)
        SignIn.save()
        messages.success(request, 'Your Message Has Been Sent.')
    return render(request, 'signin.html')


def contactinfo(request):
    form = Contact.objects.all()
    context = {'form':form}
    return render(request, 'contactform.html', context)

def jobforminfo(request):
    info = JobForm.objects.all()
    context1 = {'info':info}
    return render(request, 'jobforminfo.html', context1)

def Signin_info(request):
    info1 = signin.objects.all()
    context = {'info1':info1}
    return render(request, 'Signin_info.html', context)