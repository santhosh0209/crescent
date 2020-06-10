from django.shortcuts import render
from .models import blog

# Create your views here.
def index(request):
    return render (request, "index.html")

def about(request):
    return render (request, "about.html")

def course(request):
    return render (request, "course.html")

def staff(request):
    return render (request, "staff.html")


def blogview(request):
    context = blog.objects.all()
    return render (request, "singleblog.html", {'blog':context})


def contact(request):
    return render (request, "contact.html")