from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

from django.core.exceptions import ValidationError
from django.core.validators import MaxLengthValidator,MinLengthValidator,MinValueValidator,MaxValueValidator

# Create your views here.
'''
types of views
function based views
class based view :cbv help to structure your code  in organized ,reuseable,
modular way and follow object oriented priciples

#main aim to organized code according to http request (get,post etc...)
'''

def validate_phone(value):
    if not str(value).startswith("+977"):
        raise ValidationError("nepal ko name +977 bata nai start hunu paro")
from multiselectfield import MultiSelectField
    
choice_field=(
     ('1',"Male"),
     ('2','Female'),
     ('3','Others')
    )

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=200,validators=[MinLengthValidator(2),MaxLengthValidator(5)])
    age=models.IntegerField()
    phone=PhoneNumberField(blank=True,region='NP',validators=[validate_phone])
    ok=MultiSelectField(null=True,choices=choice_field,default=['1'])
    
    
class City(models.Model):
    title=models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
class Interest(models.Model):
    title=models.CharField(max_length=200)
    
    def __str__(self):
        return self.title
class Person(models.Model):
    name=models.CharField(max_length=200)
    city=models.ForeignKey(City,default="no city", on_delete=models.DO_NOTHING,blank=True,null=True) #no city gayara basxa
    interest=models.ManyToManyField(Interest)
    
    def __str__(self):
        return self.name
    
class Profile(models.Model):
    person=models.OneToOneField(Person, on_delete=models.CASCADE)
    bio=models.TextField()
    
    
    
