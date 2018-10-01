from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse


class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    body = models.TextField()
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    pub_date = models.DateField()

    def __str__(self):
        return self.title

    def short_body(self):
        return self.body[:255]

    def get_absolute_url(self):
        return reverse('post.detail', args=[str(self.id)])

# 3. Category
#     id = int
#     name = varchar
#
# 4. Tag
#     id = int
#     name = varchar
#
# 5. Tag_Post
#     tag_id = int
#     post_id = int
#
# 6. Comments
