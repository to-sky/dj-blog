from django.urls import path

from blog.views import PostDetailView, PostListView

urlpatterns = [
    path('', PostListView.as_view(), name='posts.list'),
    path('post/<int:pk>', PostDetailView.as_view(), name='post.detail')
]
