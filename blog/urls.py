from django.urls import path
from blog.views import PostDetailView, PostListView
from blog import views

urlpatterns = [
    path('', PostListView.as_view(), name='posts.list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post.detail'),
    path('posts', views.post_filter),
]
