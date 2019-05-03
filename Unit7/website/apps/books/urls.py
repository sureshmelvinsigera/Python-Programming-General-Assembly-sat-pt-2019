from django.contrib import admin
from django.urls import path
from apps.books import views

urlpatterns = [
    path('', views.index, name='index'),
    path('create/', views.create_book, name='create'),
    path('update/<int:pk>', views.update_book, name='update'),
    path('delete/<int:pk>', views.delete_book, name='delete'),
]
