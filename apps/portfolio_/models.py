# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

class QueryManager(models.Manager):
    def validate_query(request, postData):
        errors = {}

        if len(postData['subject']) < 3:
            errors['subject'] = "Subject must be longer than 3 characters"

        if len(postData['name']) < 3:
            errors['name'] = "Name must be longer than 3 characters"

        if len(postData['company']) < 3:
            errors['company'] = "Company must be longer than 3 characters"

        if len(postData['email']) < 3:
            errors['email'] = "Email must be longer than 3 characters"

        if len(postData['body']) < 3:
            errors['body'] = "Message must be longer than 3 characters"

        if len(postData['phone']) < 3:
            errors['phone'] = "Phone must be longer than 3 characters"
        
        return errors

class Query(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=50)
    company = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    body = models.CharField(max_length=200)
    phone = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # Inherits the Query Manager for errors
    objects = QueryManager()