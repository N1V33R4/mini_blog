from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User, BlogPost, Blogger, Comment


admin.site.register(User, UserAdmin)


class CommentInline(admin.StackedInline):
  model = Comment
  extra = 0


class BlogPostInline(admin.StackedInline):
  model = BlogPost
  extra = 0


@admin.register(Blogger)
class BloggerAdmin(admin.ModelAdmin):
  list_display = ('user', 'bio')
  inlines = [BlogPostInline]


@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
  list_display = ('title', 'author', 'created_at', 'updated_at')
  inlines = [CommentInline]


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
  list_display = ('id', 'content', 'author', 'blog', 'created_at')
