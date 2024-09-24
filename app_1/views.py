from django.shortcuts import render
from django.shortcuts import render
from app_1.models import training 
from django.http import HttpResponse
from app_1 import views
# from .models import training
# Create your views here.
# from django.http import HttpResponse
# def home(request):
#     return (request,('Home.html'))

def home (request):
    if request.method =='POST':
        training_name=request.POST['training_name']
        training_provider= request.POST ['training_provider']
        description =request.POST ['description']

        if len(training_name)<3:
             return HttpResponse ('please Ether proper training name')
        else:
            training_list=training(training_name=training_name,training_provider=training_provider,description=description)
            training_list.save()
    return render(request,'home.html',{})