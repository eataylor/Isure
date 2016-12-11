from __future__ import unicode_literals

from django.db import models

 
from django.contrib import admin

from django import forms
from decimal import Decimal

from intersure import settings 
#from Isure.forms import Directoryform
#from multiselectfield import MultiSelectField
"""
pip install django-phonenumber-field

"""


from phonenumber_field.modelfields import PhoneNumberField
#from  localflavor.us.models import PhoneNumberField 
#from  localflavor.us.forms import USPhoneNumberField

from tagging.fields import TagField

"""
MY_CHOICES = (
    ('blue', 'Blue'),
    ('green', 'Green'),
    ('black', 'Black'),
)
"""
LinkTypes = (
    ('pdf', 'PDF'),
    ('event', 'Event'),
     
)

# Create your models here.


class Commercials(models.Model):
      Name = models.CharField(max_length=80)

      def __unicode__(self):
        return self.Name
       

      class Meta:
        verbose_name_plural = "Commercial Lines"

class Personals(models.Model):
      Name = models.CharField(max_length=80)


      def __unicode__(self):
        return self.Name
       

      class Meta:
        verbose_name_plural = "Personal Lines"






class Directory(models.Model):
    AgencyName = models.CharField(max_length=75)
    BusinessType = models.CharField(max_length=30)
    PrimaryContactFN = models.CharField(max_length=40)
    PrimaryContactLN = models.CharField(max_length=40)
    ContactTitle = models.CharField(max_length=30)
    ContactEmail = models.EmailField()
    DirectLine = PhoneNumberField()

    HQAddress = models.CharField(max_length=50)
    HQAddress2 = models.CharField(max_length=50,blank=True)
    HQCity = models.CharField(max_length=50)
    HQState = models.CharField(max_length=30)
    HQZip = models.CharField(max_length=15)
    HQCountry = models.CharField(max_length=30)

    HQLat = models.DecimalField(max_digits=10, decimal_places=8,default=Decimal('0.00000'))
    HQLong = models.DecimalField(max_digits=11, decimal_places=8,default=Decimal('0.00000'))

    Differentiator = models.TextField(max_length=4000) 
    
    KeyContactFN = models.CharField(max_length=35,blank=True)
    KeyContactLN = models.CharField(max_length=35,blank=True)
    KeyContactEmail = models.EmailField(max_length=35,blank=True)
    KeyContactPhone = PhoneNumberField(blank=True)

    url = models.CharField(max_length=175,blank=True)

    CRM = models.CharField("Customer Relationship Mgmt",max_length=25,blank=True)
    AMS = models.CharField("Account Mgmt System ",max_length=25,blank=True) 

    CommPct = models.DecimalField("Commercial Percent",max_digits=4, decimal_places=2,default=Decimal('00.00'))
    BenePct = models.DecimalField("Benefits Percent",max_digits=4, decimal_places=2,default=Decimal('00.00'))
    PersPct = models.DecimalField("Persaonal Percent",max_digits=4, decimal_places=2,default=Decimal('00.00'))
    
    employees = models.PositiveSmallIntegerField("Employees",default=0)
    principals = models.PositiveSmallIntegerField("Principals",default=0)
    
    awards1 = models.TextField("Top Awards1",max_length=600,blank=True)
    awards2 = models.TextField("Top Awards2",max_length=600,blank=True)
    awards3 = models.TextField("Top Awards3",max_length=600,blank=True)
    
    goals1 = models.TextField("Top Goals1",max_length=500,blank=True)
    goals2 = models.TextField("Top Goals2",max_length=500,blank=True)
    goals3 = models.TextField("Top Goals3",max_length=500,blank=True)

    Revenue = models.DecimalField(max_digits=11, decimal_places=2,default=Decimal('0000.00'))

    Image = models.FileField(upload_to='Pics',blank=True)
 

    commercialLines = models.ManyToManyField(Commercials,blank=True)
    personalLines = models.ManyToManyField(Personals,blank=True)

    tags = TagField(max_length=1000)
    

    #favs = MultiSelectField(choices=MY_CHOICES)
   
    class Meta:
        verbose_name_plural = "Directory"

class AccessList(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()

    class Meta:
        verbose_name_plural = "Access List"



class EmailContact(models.Model):
      date = models.DateField()
      pagesource = models.CharField(max_length=50)
      receivedfrom = models.CharField(max_length=75) 
      sentto = models.CharField(max_length=75)
      content = models.TextField() 



class Event(models.Model):
      EventSummary = models.CharField(max_length=50)
      EventText = models.TextField()

      class Meta:
        verbose_name_plural = "Events"

class PressRel(models.Model):
    postDate = models.DateField()
    blurb = models.CharField(max_length=250,)
    filename = models.FileField(upload_to='Docs')
    publish = models.BooleanField()
     
    class Meta:
        verbose_name_plural = "Press Release"

class LocalLinks(models.Model):
    postDate = models.DateField()
    blurb = models.CharField(max_length=250,)
    link = models.CharField(max_length = 50)
    publish = models.BooleanField()
     
    class Meta:
        verbose_name_plural = "Local Links"


class QuickLinks(models.Model):
    Linktype = models.CharField(max_length=10,choices=LinkTypes)
    filename = models.CharField(max_length=200,blank=True)
    eventname = models.CharField(max_length=200,blank=True)
    event_id = models.ForeignKey(Event,blank=True,null=True)

    class Meta:
        verbose_name_plural = "QuickLinks"


"""
from tagging.registry import register
from tagging.registry import AlreadyRegistered
from tagging.models import Tag

     

try:
    register(Directory)
except  AlreadyRegistered:
    pass 
"""    
     
     
