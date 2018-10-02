from blog.models import Post

from django.core.management.base import BaseCommand
from faker import Faker


fake = Faker('en_US')

class Command(BaseCommand):

    def handle(self, *args, **options):
        count = input("Enter count of posts: ")
        for i in range(int(count)):

            new_post = Post.objects.create(
                title=fake.sentence(),
                body=fake.text(max_nb_chars=1000),
                author_id=1,
                pub_date=fake.date_between(start_date="-30d", end_date="today")
            )

            new_post.save()
