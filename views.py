from django.shortcuts import render
from .models import Task
from .forms import UserForm


def index(request):
    return render(request, 'main/index.html')


def about(request):
    return render(request, 'main/about.html')


def section1(request):
    return render(request, 'main/section1.html')


def section2(request):
    return render(request, 'main/section2.html')


def section3(request):
    return render(request, 'main/section3.html')


def section4(request):
    return render(request, 'main/section4.html')


def section5(request):
    return render(request, 'main/section5.html')


def section6(request):
    return render(request, 'main/section6.html')


def section7(request):
    return render(request, 'main/section7.html')


def test(request):
    return render(request, 'main/test.html')
