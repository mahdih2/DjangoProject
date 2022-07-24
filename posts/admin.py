from django.contrib import admin
from .models import Post, Comment

# Register your models here.



class CommentAdminInline(admin.TabularInline):
    model = Comment
    fields = ['text',]
    extra: int = 0



@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = [
        'id',
        'title',
        'is_enable',
        'create_date',
    ]
    inlines: list = [CommentAdminInline]


