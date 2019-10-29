from django.contrib import admin
from blogapp.models import Article, Comment, Category


# Register your models here.

class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'post', 'date', 'moderation')
    list_filter = ('date', 'name', 'moderation')


class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'category', 'author', 'date', 'moderation')
    list_filter = ('category', 'date', 'author', 'moderation')


admin.site.register(Article, ArticleAdmin)
admin.site.register(Comment, CommentAdmin)
admin.site.register(Category)
