from django.shortcuts import render, redirect
from .models import User
import mysql.connector

from django.contrib import messages
from operator import itemgetter


def welcome(req):
    return render(req, 'welcome.html')


def login(req):
    return render(req, 'login.html')


def register(req):
    if req.method == "POST":
        user = User()

        user.fname = req.POST['fname']
        user.lname = req.POST['lname']
        user.email = req.POST['email']
        user.password = req.POST['password']
        user.repassword = req.POST['repassword']
        
        print(user.password)
        if user.password != user.repassword:
            return redirect('register')
        elif user.fname == "" or user.password == "":
            messages.info(req, 'some fields are empty')
            return redirect('register')
        else:
            user.save()

    return render(req, 'register.html')
