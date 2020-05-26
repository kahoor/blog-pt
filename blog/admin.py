from django.contrib import admin

from .models import Post
# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'id', 'created', 'status', 'user')
    list_filter = ('status', 'created')
    prepopulated_fields = {'slug': ('title',)}
    ordering = ('status', 'created')
    search_fields = ('title', 'summary', 'body')


