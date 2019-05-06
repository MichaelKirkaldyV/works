# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
import smtplib

def home(request):
	return render(request, 'portfolio_/home.html')

def work(request):
	return render(request, 'portfolio_/work.html')

def about(request):
	return render(request, 'portfolio_/about.html')

def contact(request):
	return render(request, 'portfolio_/contact.html')

def resume(request):
	return render(request, 'portfolio_/resume.html')

def form_process(request):
	return redirect()