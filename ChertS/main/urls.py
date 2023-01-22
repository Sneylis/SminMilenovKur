from django.urls import path
from . import views

urlpatterns = [
    path('',views.index, name='home'),
    path('about/', views.about, name='about'),
    path('abiturients/', views.abiturients, name='abiturients'),
    path('vacation/', views.vacation, name='vacation'),
    path('post/<int:post_id>', views.showpost, name='post'),
]