from django.shortcuts import render, redirect
from django.http import JsonResponse
from . import models

def index(request):
    return render(request, 'index.html')

