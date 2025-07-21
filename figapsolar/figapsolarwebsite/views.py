from django.shortcuts import render

# Create your views here.

def index(request):

    return render(request, 'figapsolarwebsite/index.html')

def secondpage(request):
    return render(request, 'figapsolarwebsite/i.html')
