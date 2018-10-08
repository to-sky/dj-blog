from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from blog.models import Post


def post_filter(request):
    if 'author' in request.GET:
        posts = Post.objects.filter(author=request.GET['author'])
    elif 'category' in request.GET:
        if request.GET['category'] == 'None':
            posts = Post.objects.filter(category__isnull=True)
        else:
            posts = Post.objects.filter(category=request.GET['category'])
    return render(request, 'blog/post_list.html', {'post_list': posts})


def profile(request):
    return render(request, 'account/profile.html')


class PostListView(ListView):
    model = Post
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
