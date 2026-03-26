from django.http import HttpRequest, HttpResponse
from django.shortcuts import get_object_or_404, render
from django.utils import timezone
from .models import Post

def index(request: HttpRequest) -> HttpResponse:
    # Load all published posts in reverse chronological order
    posts = Post.objects.filter(published_at__lte = timezone.now()).order_by('-published_at').select_related('author')
    return render(request, "blog/index.html", {"posts": posts})

def welcome(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/welcome.html")

def post_detail(request: HttpRequest, post_id: str) -> HttpResponse:
    post = get_object_or_404(
        Post.objects.select_related('author'),
        id=post_id,
        published_at__lte=timezone.now()
    )
    return render(request, "blog/post_detail.html", {"post": post})