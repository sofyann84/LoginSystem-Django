from django.shortcuts import render

def welcome(req):
    return render(req,'welcome.html')

def login(req):
    return render(req,'login.html')

def register(req):
    return render(req,'register.html')
