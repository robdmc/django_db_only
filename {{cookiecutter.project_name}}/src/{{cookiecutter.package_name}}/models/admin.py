{% if cookiecutter.use_admin == "yes" -%}
"""
Django admin configuration for models.
Register your models here to make them available in the admin interface.
"""
from django.contrib import admin
from .example import Author, Book, Category, BookCategory


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    """Admin interface for Author model."""
    list_display = ['name', 'email', 'created_at', 'book_count']
    list_filter = ['created_at']
    search_fields = ['name', 'email']
    readonly_fields = ['created_at']
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('name', 'email')
        }),
        ('Details', {
            'fields': ('bio',)
        }),
        ('Timestamps', {
            'fields': ('created_at',),
            'classes': ('collapse',)
        }),
    )
    
    def book_count(self, obj):
        """Display the number of books by this author."""
        return obj.books.count()
    book_count.short_description = 'Books'


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """Admin interface for Category model."""
    list_display = ['name', 'description', 'book_count']
    search_fields = ['name', 'description']
    
    def book_count(self, obj):
        """Display the number of books in this category."""
        return obj.book_set.count()
    book_count.short_description = 'Books'


class BookCategoryInline(admin.TabularInline):
    """Inline admin for BookCategory through model."""
    model = BookCategory
    extra = 1
    readonly_fields = ['added_at']


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    """Admin interface for Book model."""
    list_display = ['title', 'author', 'published_date', 'pages', 'is_available', 'created_at']
    list_filter = ['is_available', 'published_date', 'author', 'categories']
    search_fields = ['title', 'author__name', 'isbn']
    readonly_fields = ['created_at', 'updated_at']
    date_hierarchy = 'published_date'
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'author', 'isbn')
        }),
        ('Publication Details', {
            'fields': ('published_date', 'pages', 'is_available')
        }),
        ('Timestamps', {
            'fields': ('created_at', 'updated_at'),
            'classes': ('collapse',)
        }),
    )
    
    inlines = [BookCategoryInline]
    
    def get_queryset(self, request):
        """Optimize queries with select_related."""
        return super().get_queryset(request).select_related('author')


@admin.register(BookCategory)
class BookCategoryAdmin(admin.ModelAdmin):
    """Admin interface for BookCategory through model."""
    list_display = ['book', 'category', 'added_at']
    list_filter = ['category', 'added_at']
    readonly_fields = ['added_at']
    
    def get_queryset(self, request):
        """Optimize queries with select_related."""
        return super().get_queryset(request).select_related('book', 'category')
{%- endif %}