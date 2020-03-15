from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'blog'

urlpatterns = [

    path('', views.index, name='index'),
    path('create/', views.create_blog, name='create-blog'),
    path('<slug>/', views.blog_detail, name='detail-blog'),


]