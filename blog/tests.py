from datetime import timedelta
from uuid import uuid4

from django.test import TestCase
from django.urls import reverse
from django.utils import timezone

from blog.models import Author, Post


class BlogViewTests(TestCase):
    def setUp(self) -> None:
        self.author = Author.objects.create(
            id=uuid4(),
            full_name="Author Example",
            created_at=timezone.now(),
            modified_at=timezone.now(),
        )

    def create_post(self, title: str, published: bool = True, offset_days: int = 0) -> Post:
        return Post.objects.create(
            id=uuid4(),
            title=title,
            body="Sample body",
            author=self.author,
            created_at=timezone.now(),
            modified_at=timezone.now(),
            published_at=timezone.now() - timedelta(days=offset_days) if published else timezone.now() + timedelta(days=365),
        )

    def test_homepage_loads(self) -> None:
        response = self.client.get(reverse("welcome"))
        self.assertEqual(response.status_code, 200)

    def test_index_page_lists_only_published(self) -> None:
        visible = self.create_post("Visible Post", published=True)
        self.create_post("Hidden Post", published=False)

        response = self.client.get(reverse("index"))
        posts = response.context["posts"]

        self.assertIn(visible, posts)
        self.assertEqual(posts.count(), 1)

    def test_index_ordering_newest_first(self) -> None:
        older = self.create_post("Old", offset_days=2)
        newer = self.create_post("New", offset_days=0)

        response = self.client.get(reverse("index"))
        posts = list(response.context["posts"])

        self.assertEqual(posts[0], newer)
        self.assertEqual(posts[1], older)

    def test_detail_page_success(self) -> None:
        post = self.create_post("Detail Post")

        response = self.client.get(reverse("post_detail", args=[post.id]))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Detail Post")

    def test_detail_page_not_found(self) -> None:
        response = self.client.get(reverse("post_detail", args=[uuid4()]))

        self.assertEqual(response.status_code, 404)

    def test_markdown_rendering(self) -> None:
        post = Post.objects.create(
            id=uuid4(),
            title="Markdown",
            body="# Title\n\n**bold text**",
            author=self.author,
            created_at=timezone.now(),
            modified_at=timezone.now(),
            published_at=timezone.now(),
        )

        response = self.client.get(reverse("post_detail", args=[post.id]))

        self.assertContains(response, "<h1>Title</h1>", html=True)
        self.assertContains(response, "<strong>bold text</strong>", html=True)