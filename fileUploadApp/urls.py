from django.urls import path
from fileUpload import settings
from . import views
from django.conf.urls import static

urlpatterns = [
    path('', views.index, name='index'),
    path('details/', views.details, name='details'),
]