from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.views.generic import CreateView

from .forms import AddNewsForm
from .models import News
# Create your views here.

def index(request):
    news = News.objects.all()
    news = reversed(news)

    return render(request, 'main/index.html', {'news':news} )

def about(request):
    return render(request, 'main/about.html')

def abiturients(request):
    return render(request,'main/abiturients.html')

def vacation(request):
    return render(request,'')

def showpost (request, post_id):
    news = News.objects.filter(pk=post_id)
    return render(request, 'main/showpost.html', {'news':news})

def addNews (request):
    if request.method == 'POST':
        form = AddNewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddNewsForm()
    return render(request, 'main/addNews.html', {'form':form})
