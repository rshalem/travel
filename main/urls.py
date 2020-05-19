from django.urls import path, re_path
from . import views
from django.conf import settings
from django.conf.urls.static import static

# defining app name, to use it in namespaces ie main:home, main:logout etc
app_name = 'main'

# url patterns list

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('explore/', views.explore, name='explore'),
    path('explore/<int:state_id>', views.state_detail, name='state_detail'),

    path('explore/place/<int:state_id>', views.city_detail, name= 'city_detail'),
    #url(r'^explore/(?P<state_id>[0-9]+)/(?P<s_id>[0-9]+)/$', views.city_detail, name='city_detail'),

    path('sign-up/', views.sign_up, name='sign_up'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    #path('add-place/', views.add_place, name='add-place'),

]


# this is the url reference for browser to access the media files from our OS/computer

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)