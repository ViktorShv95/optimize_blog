from django.contrib import admin
from blog.models import Post, Tag, Comment

@admin.register(Post)
class PostModelAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'likes')


@admin.register(Tag)
class TagModelAdmin(admin.ModelAdmin):
    pass


@admin.register(Comment)
class CommentModelAdmin(admin.ModelAdmin):
    raw_id_fields = ('author', 'post')