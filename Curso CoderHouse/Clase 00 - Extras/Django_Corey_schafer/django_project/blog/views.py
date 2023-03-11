from django import http
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse('<h1>Blog Home</h1>')
# Create your views here.

def about(request):
    return HttpResponse('<h1>About Blog</h1>')