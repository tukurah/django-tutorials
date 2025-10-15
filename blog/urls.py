
from django.urls import path
from . import views

urlpatterns = [
    path('', views.blogHome, name="blogHome"),
    path('new/', views.addBlog, name="addBlog"),
    path('<int:pk>/', views.blogDetails, name="blogDetails"),
    path("delete/<int:pk>/", views.deleteBlog, name="deleteBlog"),
    

]