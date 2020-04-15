from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView

from .models import Blogpost, Comment
from .forms import CommentForm

from newsapi import NewsApiClient


def home(request):
    newsapi = NewsApiClient(api_key='313c12fcfda3465f89f36b377c088e3b')
    top = newsapi.get_top_headlines(q='coronavirus',
                                    language='en')

    l = top['articles']
    desc = []
    news = []
    img = []

    for i in range(len(l)):
        f = l[i]
        news.append(f['title'])
        desc.append(f['description'])
        img.append(f['urlToImage'])
    mylist = zip(news, desc, img)

    return render(request, 'home.html', context={"mylist": mylist})



def about(request):
    return render(request, 'about.html')


def blogposts_index(request):
    blogposts = Blogpost.objects.filter(user=request.user)
    return render(request, 'blogposts/index.html', {'blogposts': blogposts})


def blogposts_all(request):
    blogposts = Blogpost.objects.all()
    return render(request, 'blogposts/get_all_posts.html', {'blogposts': blogposts})


def blogposts_detail(request, blogpost_id):
    blogpost = Blogpost.objects.get(id=blogpost_id)
    return render(request, 'blogposts/detail.html', {'blogpost': blogpost})


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


def add_comment(request, blogpost_id):
    form = CommentForm(request.POST)
    if form.is_valid():
        new_comment = form.save(commit=False)
        new_comment.blogpost_id = blogpost_id
        new_comment.save()
    return redirect('detail', blogpost_id=blogpost_id)


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
