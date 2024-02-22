from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact_us.html')

def gallery(request):
    return render(request, 'gallery.html')

# Create your views here.
