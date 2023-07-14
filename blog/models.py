from django.contrib.auth.models import AbstractUser
from django.db import models
from django.urls import reverse


class User(AbstractUser):
  pass


class Blogger(models.Model):
  user = models.OneToOneField(User, on_delete=models.CASCADE)
  bio = models.TextField(help_text='Description of the blogger\' life. Or some wacky adventures you might think up.')

  class Meta:
    ordering = ['user']

  def __str__(self) -> str:
    return self.user.username
  
  def get_absolute_url(self):
    return reverse('blogger-detail', args=[str(self.pk)])


class BlogPost(models.Model):
  title = models.CharField(max_length=200)
  content = models.TextField(max_length=5000, help_text='What you would like to share to your readers.')
  author = models.ForeignKey(Blogger, on_delete=models.SET_NULL, null=True)
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    ordering = ['-created_at']

  def __str__(self) -> str:
    return self.title
  
  def get_absolute_url(self):
    return reverse('blog-detail', args=[str(self.pk)])


class Comment(models.Model):
  author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
  content = models.TextField(max_length=500, help_text='How was the blog post?')
  blog = models.ForeignKey(BlogPost, on_delete=models.SET_NULL, null=True)
  created_at = models.DateTimeField(auto_now_add=True)

  class Meta:
    ordering = ['-created_at']

  def __str__(self) -> str:
    len_title = 75
    return self.content if len(self.content) < len_title else self.content[:len_title] + '...'

  def get_absolute_url(self):
    """Redirects to blog post that owns this comment."""
    return reverse('blog-detail', kwargs={'pk': self.blog.pk}) # type: ignore
  