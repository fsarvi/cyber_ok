from django.shortcuts import render

def index(request):
    return render(request, 'index.html', {})

def trabajos(request):
    return render(request, 'trabajos.html', {})

def tramites(request):
    return render(request, 'tramites.html', {})
    