from django.core.paginator import Paginator
from django.shortcuts import render,redirect

from .forms import AddBookForm
from .models import *

# Create your views here.

def library_home (request):
    contact_list = Books.objects.all().order_by("-time_create")
    cat = Category.objects.all()
    paginator = Paginator(contact_list, 4)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    return render(request, 'library/library_home.html', {'page_obj': page_obj,'cat':cat})


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


