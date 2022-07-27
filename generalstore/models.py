import datetime
from email.policy import default
from pickle import TRUE
from tkinter import CASCADE




from unittest.util import _MAX_LENGTH
from urllib import request
from django.conf import settings

from django.db import models
from django.contrib.auth.models import User
from django.forms import CharField, EmailField, IntegerField, PasswordInput
from django.test import RequestFactory


user=settings.AUTH_USER_MODEL



class category(models.Model):
    category=models.CharField(max_length=30, null=True)
    def __str__(self):
        return self.category
   

    

class gasentry(models.Model):
    supplier = models.ForeignKey(user,
    on_delete=models.SET_NULL,
    
    null=TRUE,
    limit_choices_to={'is_staff': True},
    )
    created_at = models.DateTimeField(auto_now=True,null=True )
    category=models.ForeignKey(category, on_delete=models.SET_NULL,null=True )

    quantity = models.IntegerField(
        null=TRUE,
        blank=True)
    # CATE=(('mechi','mechi'),
    #     ('koshi','koshi'),
    #     ('trisakte','trisakte'),
    #     ('parajuli','parajuli'))
  
   
    complete_firm_address=models.CharField(max_length=100,null=TRUE)
    firm_contact=models.CharField(max_length=10,null=TRUE)
    Email=models.EmailField(max_length=50,null=TRUE)
    gasentrymanager=models.Manager()
    # def __str__(self):
    #     return self.quantity
 



class gasondemand(models.Model):
    specified_supplier=models.ForeignKey(gasentry,on_delete=models.PROTECT, null=True)
    supplier=models.CharField(max_length=30,null=True)
    Customer_name=models.CharField(max_length=30,null=TRUE)
    required_quantity=models.IntegerField(null=True)
    customer_contact=models.IntegerField(null=True)
    customer_address=models.CharField(max_length=100,null=True)
    gas_category=models.CharField(max_length=30,null=True)
    status=models.CharField(default='pending',max_length=30,null=True)
    created_at = models.DateTimeField(auto_now=True,null=True )
    getby=models.CharField(max_length=30,null=TRUE)
    objects=models.Manager()
   

    def __str__(self):
        return f'{self.gas_category}--{self.required_quantity}'



