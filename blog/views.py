from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.utils import timezone
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from .forms import PostForm
from .models import Post


def home(request):
    return render(request, 'home.html')


def profile(request):
    posts = Post.objects.filter(author=request.user.id)
    return render(request, 'account/profile.html', {'posts': posts})


def post_filter(request):
    posts = Post.objects.all()
    for filter in ['category', 'author', 'tag']:
        if filter in request.GET:
            if request.GET[filter] == 'None':
                posts = posts.filter(**{filter + '__isnull': True})
            else:
                posts = posts.filter(**{filter: request.GET[filter]})

    return render(request, 'blog/post_list.html', {'post_list': posts})


def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()
            form.save_m2m()

            return redirect('posts.list')
    else:
        form = PostForm()

    return render(request, 'blog/forms/post_create.html', {'form': form})


def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)

        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.pub_date = timezone.now()
            post.save()
            form.save_m2m()

            return redirect('posts.list')
    else:
        form = PostForm(instance=post)

    return render(request, 'blog/forms/post_edit.html', {'form': form, 'post': post})


def post_delete(request, pk):
    if request.method != 'POST':
        return HttpResponse(status=405)

    post = get_object_or_404(Post, pk=pk)
    post.delete()

    return HttpResponse(status=200)


def post_detail_preview(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/_post_detail_preview.html', {'post': post})


class PostListView(ListView):
    model = Post
    paginate_by = 10
    ordering = ['-pub_date']


class PostDetailView(DetailView):
    model = Post
