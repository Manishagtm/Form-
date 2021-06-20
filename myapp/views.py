from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect

# Create your views here.
from django.http import HttpResponse

from .models import tbl_Login


def index(request):
    return render(request, 'form.html')


def login(request):
    context = {'success': False}
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        pdf = request.POST.get('pdf')
        pictures = request.POST.get('pictures')

        user = tbl_Login()
        user.email = email
        user.password = password
        user.pdf = pdf
        user.pictures = pictures

        user.save()
        return redirect('/')
    else:
        return render(request, 'form.html', context)


def sign(request):
    return render(request, 'sign.html')


def two(request):
    return render(request, 'two.html')
