from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='yamashiro'),
    path('post/<int:pk>/', views.post_detail, name='michishio'),
    path('post/new', views.post_new, name='post_new'),
    path('post/<int:pk>/edit/', views.post_edit, name='asashio'),
]