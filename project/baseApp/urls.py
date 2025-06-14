from django.urls import path
from .views import HomeView,Child
urlpatterns = [
    path("",HomeView.as_view(),name="home"), #it is method which is used to convert class base into funciton base so that django url systme can be use
    path("child/",Child.as_view())
]
