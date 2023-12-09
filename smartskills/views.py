from django.shortcuts import render

def home(request):
    return render(request, 'main.html')

def auth(request):
    return render(request, 'auth.html')

def registration(request):
    return render(request, 'registration.html')

def pyqt5(request):
    return render(request, 'pyqt5.html')

def django(request):
    return render(request, 'django.html')

def python(request):
    return render(request, 'python.html')

def bootstrap(request):
    return render(request, 'bootstrap.html')

def profile(request):
    return render(request, 'profile.html')

def wrong(request):
    return render(request, 'wrong.html')
