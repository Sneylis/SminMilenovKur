from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.views import LoginView
from django.core.paginator import Paginator
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import AddNewsForm, RegisterUserForm
from .models import News
# Create your views here.
from .utils import DataMixin


def index(request):
    contact_list = News.objects.all().order_by("-time_create")
    paginator = Paginator(contact_list, 4)
    page_num = request.GET.get('page')
    page_obj = paginator.get_page(page_num)

    return render(request, 'main/index.html', {'page_obj':page_obj} )

def about(request):
    return render(request, 'main/about.html')

def abiturients(request):
    return render(request,'main/abiturients.html')

def vacation(request):
    return render(request,'')

def showpost (request, post_id):
    news = News.objects.filter(pk=post_id)
    return render(request, 'main/showpost.html', {'news':news})


@login_required
def addNews (request):
    if request.method == 'POST':
        form = AddNewsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = AddNewsForm()
    return render(request, 'main/addNews.html', {'form':form})

class register(DataMixin, CreateView):
    form_class = RegisterUserForm
    template_name = 'main/register.html'
    success_url = reverse_lazy('home')

    def get_context_data(self,object_list=None,**kwargs):
        context=super().get_context_data(**kwargs)
        return dict(list(context.items()))

class login(DataMixin,LoginView):
    form_class = AuthenticationForm
    template_name = 'main/login.html'

    def get_context_data(self, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        return dict(list(context.items()))

    def get_success_url(self):
        return reverse_lazy('home')

@login_required()
def profile(request):
    return render(request,'main/profile.html',{'request':request})
