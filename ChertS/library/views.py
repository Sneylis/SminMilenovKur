from django.shortcuts import render,redirect

from .forms import AddBookForm
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

def show_book(request, sbook_id):
    books = Books.objects.filter(pk=sbook_id)

    return render(request, 'library/book.html', {'books':books})

def AddBooks(request):
    if request.method == 'POST':
        form = AddBookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('library')
    else:
        form = AddBookForm()
    return render(request, 'library/addBook.html', {'form': form})


