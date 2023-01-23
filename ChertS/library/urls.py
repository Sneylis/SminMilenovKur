from django.urls import path
from . import views

urlpatterns = [
    path('', views.library_home, name='library'),
    path('category/<int:cat_id>/', views.show_category, name='category'),
    path('sbook/<int:sbook_id>/', views.show_book, name='sbook'),
    path('addBook/', views.AddBooks, name='addBook'),


]