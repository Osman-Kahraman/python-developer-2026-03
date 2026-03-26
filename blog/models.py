import uuid
from django.db import models

class Author(models.Model):
	"""
	Represents an author of blog posts.
	Fields:
		id: Unique identifier (UUID) for the author.
		full_name: The full name of the author.
		created_at: Timestamp when the author was created (from data).
		modified_at: Timestamp when the author was last modified (from data).
	"""
	
	id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
	full_name = models.CharField(max_length = 255)
	created_at = models.DateTimeField()
	modified_at = models.DateTimeField()

	def __str__(self) -> str:
		return self.full_name


class Post(models.Model):
	"""
	Represents a blog post.
	Fields:
		id: Unique identifier (UUID) for the post.
		title: Title of the post.
		body: Content of the post (Markdown supported).
		created_at: Timestamp when the post was created (from data).
		modified_at: Timestamp when the post was last modified (from data).
		published_at: Timestamp when the post was published (from data).
		author: ForeignKey to the Author who wrote the post.
	"""
	
	id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
	title = models.CharField(max_length = 255)
	body = models.TextField()
	created_at = models.DateTimeField()
	modified_at = models.DateTimeField()
	published_at = models.DateTimeField()
	author = models.ForeignKey(Author, on_delete = models.CASCADE)

	def __str__(self) -> str:
		return self.title
