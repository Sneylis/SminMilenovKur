from django.urls import path
from . import views

urlpatterns = [
    path('', views.vacations_home, name='vacation'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
    path('vac/<int:vac_id>/', views.show_vacation, name='vac'),
    path('Doc/', views.AddDocs, name='addDoc'),
]
