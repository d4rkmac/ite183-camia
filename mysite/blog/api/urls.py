from django.urls import path
from . import views

urlpatterns = [
    path('', views.viewPosts),
    path('add/', views.addPost),
    path('postdetail/<str:pk>/', views.viewPostDetail),
    path('update/<str:pk>/', views.updatePost),
    path('delete/<str:pk>/', views.deletePost),
]