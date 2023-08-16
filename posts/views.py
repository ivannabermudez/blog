from django.views.generic import ListView, DetailView
from django .views.generic.edit import CreateView
from django.shortcuts import render
from .models import Post

class PostListView(ListView):
    template_name = "posts/list.html"
    model = Post  #get data sorted list view for django 

class PostDetailView(DetailView):
    template_name = "posts/detail.html"
    model = Post


class PostCreateView(CreateView):
    template_name = "posts/new.html"
    model = Post
    fields = ["title", "subtitle", "body"]


def add_post_view(request):
    # Your view logic here
    return render(request, 'add_post.html')