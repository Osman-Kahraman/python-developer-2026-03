from django.http import HttpRequest, HttpResponse
from django.shortcuts import render
from .models import Post
from django.utils import timezone
from django.shortcuts import get_object_or_404

def index(request: HttpRequest) -> HttpResponse:
    # Load all published posts in reverse chronological order
    posts = Post.objects.filter(published_at__lte = timezone.now()).order_by('-published_at').select_related('author')
    return render(request, "blog/index.html", {"posts": posts})

def welcome(request: HttpRequest) -> HttpResponse:
    return render(request, "blog/welcome.html")

def post_detail(request: HttpRequest, post_id) -> HttpResponse:
    post = get_object_or_404(
        Post.objects.select_related('author'),
        id=post_id,
        published_at__lte=timezone.now()
    )
    return render(request, "blog/post_detail.html", {"post": post})