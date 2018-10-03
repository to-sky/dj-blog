from django.contrib import admin
from .models import Post, Category, Tag


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'pub_date', 'category')


admin.site.register(Category)
admin.site.register(Tag)
