from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from blog.models import Post


def profile(request):
    return render(request, 'account/profile.html')


class PostListView(ListView):
    model = Post
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
