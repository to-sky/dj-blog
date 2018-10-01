from blog.models import Post
import datetime

from django.core.management.base import BaseCommand
from faker import Faker


fake = Faker('en_US')

class Command(BaseCommand):
    count = input("Enter count of posts: ")
    for i in range(int(count)):

        new_post = Post.objects.create(
            title=fake.sentence(),
            body=fake.text(),
            author_id=1,
            pub_date=datetime.today()
        )

        new_post.save()
