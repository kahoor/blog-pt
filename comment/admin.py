from django.contrib import admin

from .models import Comment 
# Register your models here.
@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ['user', 'body', 'created', 'active', 'post',]
    actions = [ 'approve_comments']

    def approve_comments(self, request, queryset):
        queryset.update(active=True)