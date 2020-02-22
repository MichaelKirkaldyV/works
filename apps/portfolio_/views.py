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
	errors = Query.objects.validate_query(request.POST)

	if len(errors):
		for tag, error in errors.items():
			messages.error(request, error)
		return redirect('/contact')
	
	else:
		#Make connection with smtp instance
		server = smtplib.SMTP('smtp.gmail.com',587)
		#Identify as Gmail Client
		server.ehlo()
		#Secure email with tls encryption
		server.starttls()
		#Re-Identify with encrpted connection
		server.ehlo()

		server.login('kirkaldymichaelv@gmail.com', 'afszipzhfurcupei')

		subject = request.POST['subject']
		body = request.POST['body']
		client_email = request.POST['email']
		name = request.POST['name']
		phone = request.POST['phone']

		msg = 'subject: {}\n\n{}\n\n{}\n\n{}'.format(name, subject, client_email, phone, body)

		server.sendmail(client_email, 'kirkaldymichaelv@gmail.com', msg)
		return redirect('/success')


def success(request):
	return render(request, 'portfolio_/success.html')