from django.urls import path
from .views import IndexView,CreateData,UpdateData,DeleteData
urlpatterns = [
    path("",IndexView.as_view(),name="index"),
    path("create/",CreateData.as_view(),name="create"),
    path("update/<pk>",UpdateData.as_view(),name="update"),
    path("delete/<pk>",DeleteData.as_view(),name="delete"),
]
