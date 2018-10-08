from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100, help_text='Post title')
    body = models.TextField(help_text='Post content')
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    pub_date = models.DateField()
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True)
    tag = models.ManyToManyField('Tag', help_text='Select a text for this post')

    def __str__(self):
        return self.title

    def short_body(self):
        return self.body[:255] + '...'

    def get_absolute_url(self):
        return reverse('post.detail', args=[str(self.id)])


class Category(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

# 6. Comments
