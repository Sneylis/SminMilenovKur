from django.core.paginator import Paginator
from django.shortcuts import render, redirect

from .forms import AddDocs
from .models import *


# Create your views here.

def vacations_home (request):
    contact_list = Vacations.objects.all()
    cat = VacationsCategory.objects.all()
    paginator = Paginator(contact_list, 4)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    return render(request, 'vacations/vacations.html', {'page_obj': page_obj,'cat':cat})


def show_category (request,cat_id):
    cat = VacationsCategory.objects.all()
    vac = Vacations.objects.filter(cat_id=cat_id)


    return render(request, 'vacations/vacations.html',{'cat':cat,'cat_selected':cat_id,'book':vac})

def show_vacation(request, vac_id):
    books = Vacations.objects.filter(pk=vac_id)

    return render(request, 'vacations/vacation.html', {'books':books})

def AddDoc(request):
    if request.method == 'POST':
        form = AddDocs(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('vacation')
    else:
        form = AddDocs()
    return render(request, 'vacations/Doc.html', {'form': form})
