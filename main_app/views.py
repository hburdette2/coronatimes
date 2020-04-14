from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Blogpost, Comment


def home(request):
    return render(request, 'home.html')


def about(request):
    return render(request, 'about.html')

def blogposts_index(request):
    blogposts = Blogpost.objects.filter(user=request.user)
    return render(request, 'blogposts/index.html', { 'blogposts' : blogposts })

def blogposts_detail(request, blogpost_id):
    blogpost = Blogpost.objects.get(id=blogpost_id)
    return render(request, 'blogposts/detail.html', { 'blogpost' : blogpost })

def signup(request):
    error_message = ''

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('/')
        else:
            error_message = 'Invalid sign up - try again'
    form = UserCreationForm()
    context = {'form': form, 'error_message': error_message}
    return render(request, 'registration/signup.html', context)

class BlogpostCreate(CreateView):
    model = Blogpost
    fields = ['title', 'body']
    success_url = '/blogposts/'

    def form_valid(self, form):
        form.instance.user = self.request.user 
        return super().form_valid(form)

class BlogpostUpdate(UpdateView):
    model = Blogpost
    fields = ['title', 'body']

class BlogpostDelete(DeleteView):
    model = Blogpost
    success_url = '/blogposts/'