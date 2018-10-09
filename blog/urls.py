from django.urls import path
from blog.views import PostDetailView, PostListView
from blog import views

urlpatterns = [
    path('', PostListView.as_view(), name='posts.list'),
    path('posts', views.post_filter, name='posts.filter'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post.detail'),
    path('post/create', views.post_create, name='post.create'),
    path('post/<int:pk>/edit', views.post_edit, name='post.edit'),
    path('post/<int:pk>/delete', views.post_delete, name='post.delete'),
]
