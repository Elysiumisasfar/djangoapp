from django.shortcuts import render
# blog/views.py
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView,  DeleteView# new
from .models import Post
from django.urls import reverse_lazy # new

from django.http import HttpResponse
from django.template import loader
def index(request):
     template = loader.get_template('blog/base.html')
     context = {}
     return HttpResponse(template.render(context, request))

class BlogListView(ListView):
    model = Post
    template_name = 'home.html'
    
class BlogDetailView(DetailView): # new
    model = Post
    template_name = 'post_detail.html'  
class BlogCreateView(CreateView): # new
    model = Post
    template_name = 'post_new.html'
    fields = '__all__'

class BlogUpdateView(UpdateView): # new
    model = Post
    template_name = 'post_edit.html'
    fields = ['title', 'body']

class BlogDeleteView(DeleteView): # new
    model = Post
    template_name = 'post_delete.html'
    success_url = reverse_lazy('home')