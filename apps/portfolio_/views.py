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
	#context manager makes sure connection is closed without needing to do manually.
	#mail server/ port no.
	print request
	server = smtplib.SMTP('smtp.gmail.com',587)
	server.ehlo()
	server.starttls()
	server.ehlo()

	server.login('kirkaldymichaelv@gmail.com', 'afszipzhfurcupei')

	subject = request.POST['subject']
	body = request.POST['body']
	client_email = request.POST['email']

	msg = 'subject: {}\n\n{}'.format(subject, body)

	server.sendmail(client_email, 'kirkaldymichaelv@gmail.com', msg)
	return redirect('/')