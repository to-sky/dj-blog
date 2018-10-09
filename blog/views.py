from django.http import HttpResponse
from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from blog.models import Post


def post_filter(request):
    posts = Post.objects.all()
    for filter in ['category', 'author', 'tag']:
        if filter in request.GET:
            if request.GET[filter] == 'None':
                posts = posts.filter(**{filter + '__isnull': True})
            else:
                posts = posts.filter(**{filter: request.GET[filter]})

    return render(request, 'blog/post_list.html', {'post_list': posts})


def profile(request):
    posts = Post.objects.filter(author=request.user.id)
    return render(request, 'account/profile.html', {'posts': posts})


def post_create(request):
    return HttpResponse('Form for create new post')


def post_edit(request, pk):
    return HttpResponse('Form for edit post')


def post_delete(request, pk):
    return HttpResponse('Delete post')


class PostListView(ListView):
    model = Post
    paginate_by = 10


class PostDetailView(DetailView):
    model = Post
