from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Courses

# Create your views here.

def home(request):
    #getting all courses from the database from course
    #objects.all means select all from course table 
    course = Courses.objects.all()
    
    # select from course table form id = ? 
    #cost = Courses.objects.get(pk=)
    
    context =  {
        "cos": course
    }
    
    mit = loader.get_template('index.html')
    return HttpResponse(mit.render(context))


def about(request):
    about = loader.get_template('about.html')
    return HttpResponse(about.render())

def studentlist(request):
    student = loader.get_template('datatable/index.html')
    return HttpResponse(student.render())
