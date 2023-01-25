from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('',views.index, name='home'),
    path('about/', views.about, name='about'),
    path('abiturients/', views.abiturients, name='abiturients'),
    path('vacation/', views.vacation, name='vacation'),
    path('post/<int:post_id>', views.showpost, name='post'),
    path('addNews/', views.addNews, name='addNews'),
    path('register/',register.as_view(),name='register'),
    path('login/',login.as_view(),name='login'),
    path('profile/',views.profile,name='profile'),
]