from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'figapsolarwebsite/index.html')

def secondpage(request):
    return render(request, 'figapsolarwebsite/i.html')

def about(request):
    return render(request, 'figapsolarwebsite/about.html')

def service(request):
    return render(request, 'figapsolarwebsite/service.html')

def project(request):
    return render(request, 'figapsolarwebsite/project.html')

def contact(request):
    return render(request, 'figapsolarwebsite/contact.html')
