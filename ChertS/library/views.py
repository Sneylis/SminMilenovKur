from django.shortcuts import render
from .models import *

# Create your views here.

def library_home (request):
    books = Books.objects.all()
    cat = Category.objects.all()


    return render(request, 'library/library_home.html', {'books':books, 'cat':cat})


def show_category (request,cat_id):
    cat = Category.objects.all()
    books = Books.objects.filter(cat_id=cat_id)


    return render(request, 'library/library_home.html',{'cat':cat,'cat_selected':cat_id,'books':books})