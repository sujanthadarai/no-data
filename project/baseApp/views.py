from django.shortcuts import render,redirect
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
    if not value.startswith("+977"):
        raise ValidationError("nepal ko name +977 bata nai start hunu paro")


from django.views import View
from .models import Student

class HomeView(View):
    def get(self,request):
        data=Student.objects.all()
        return render(request,'baseApp/home.html',{'data':data})
    
    def post(self,request):
        name=request.POST['name']
        age=request.POST['age']
        
        Student.objects.create(name=name,age=age)
        return redirect('home')
    
class Child(HomeView):
    def get(self,request):
        return super().get(request)
    