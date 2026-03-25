from django.contrib import admin

# Register your models here.
from .models import Post

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'content','published', 'created_at', 'updated_at']
    list_filter = ['published']
    search_fields = ['title', 'content']