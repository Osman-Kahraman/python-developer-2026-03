
import json
import os
from django.core.management.base import BaseCommand
from blog.models import Author, Post
from django.utils.dateparse import parse_datetime

class Command(BaseCommand):
    help = 'Import authors and posts from JSON files into the database.'

    def handle(self, *args: object, **options: object) -> None:
        # Gets the project root directory (where manage.py is located)
        from django.conf import settings

        base_dir = settings.BASE_DIR if hasattr(settings, 'BASE_DIR') else os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
        authors_dir = os.path.join(base_dir, 'data', 'authors')
        posts_dir = os.path.join(base_dir, 'data', 'posts')

        # Import authors
        self.stdout.write('Importing authors...')
        for filename in os.listdir(authors_dir):
            if filename.endswith('.json'):
                with open(os.path.join(authors_dir, filename), 'r') as f:
                    data = json.load(f)
                    Author.objects.update_or_create(
                        id=data['id'],
                        defaults={
                            'full_name': data['full_name'],
                            'created_at': parse_datetime(data['created_at']),
                            'modified_at': parse_datetime(data['modified_at'])
                        }
                    )
        self.stdout.write(self.style.SUCCESS('Authors imported.'))

        # Import posts
        self.stdout.write('Importing posts...')
        for filename in os.listdir(posts_dir):
            if filename.endswith('.json'):
                with open(os.path.join(posts_dir, filename), 'r') as f:
                    data = json.load(f)
                    Post.objects.update_or_create(
                        id=data['id'],
                        defaults={
                            'title': data['title'],
                            'body': data['body'],
                            'created_at': parse_datetime(data['created_at']),
                            'modified_at': parse_datetime(data['modified_at']),
                            'published_at': parse_datetime(data['published_at']),
                            'author_id': data['author']
                        }
                    )
        self.stdout.write(self.style.SUCCESS('Posts imported.'))
