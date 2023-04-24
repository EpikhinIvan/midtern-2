from django.shortcuts import render


def home_view(request):
    return render(request, 'home.html')

def register_view(request):
    # код функции представления
    return render(request, 'register.html')
