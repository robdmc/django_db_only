"""
Example Django models to demonstrate the ORM setup.
You can delete this file and create your own models.
"""

from django.db import models
from django.utils import timezone


class Author(models.Model):
    """Example Author model."""
    name = models.CharField(max_length=100)
    email = models.EmailField()
    bio = models.TextField(blank=True)
    created_at = models.DateTimeField(default=timezone.now)
    
    class Meta:
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Category(models.Model):
    """Example Category model."""
    name = models.CharField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    
    class Meta:
        verbose_name_plural = "categories"
        ordering = ['name']
    
    def __str__(self):
        return self.name


class Book(models.Model):
    """Example Book model with relationships."""
    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    categories = models.ManyToManyField(Category, through='BookCategory')
    isbn = models.CharField(max_length=13, unique=True, blank=True)
    pages = models.PositiveIntegerField(null=True, blank=True)
    published_date = models.DateField(null=True, blank=True)
    is_available = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    class Meta:
        ordering = ['-created_at']
        indexes = [
            models.Index(fields=['author', 'published_date']),
            models.Index(fields=['title']),
        ]
    
    def __str__(self):
        return f"{self.title} by {self.author.name}"


class BookCategory(models.Model):
    """Through model for Book-Category relationship."""
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    added_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ('book', 'category')
        ordering = ['added_at']
    
    def __str__(self):
        return f"{self.book.title} - {self.category.name}"