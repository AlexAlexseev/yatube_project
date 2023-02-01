# posts/urls.py
from django.urls import path

from . import views

app_name = 'Posts'

urlpatterns = [
    path('', views.index, name='main_page'),
    path('group_list.html', views.group_posts, name='group_posts'),
   # path('group/<slug:slug>/', views.group_posts, name='group_posts'),
] 
#, name='group_posts'