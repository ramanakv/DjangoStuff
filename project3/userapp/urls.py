
from django.urls import path
from . import views

urlpatterns = [
    path('showAll1/', views.getAll1),
    path('showAll2/', views.getAll2)
]
