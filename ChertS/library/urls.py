from django.urls import path
from . import views

urlpatterns = [
    path('', views.library_home, name='library'),
    path('category/<int:cat_id>/', views.show_category, name='category')


]