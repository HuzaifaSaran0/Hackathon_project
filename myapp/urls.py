from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login/', views.login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('about/', views.about, name='about'),
    path('blog/', views.blog_list, name='blog_list'),
]
from django.conf.urls import handler404

from .views import custom_404_view

handler404 = custom_404_view
