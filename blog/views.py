from typing import Any, Dict
from django.contrib.auth.mixins import LoginRequiredMixin
from django.forms.models import BaseModelForm
from django.http import HttpResponse
from django.views import generic
from django.shortcuts import get_object_or_404, render
from .models import Blogger, BlogPost, Comment

def index(request):
  num_bloggers = Blogger.objects.all().count()
  num_blogposts = BlogPost.objects.all().count()
  num_comments = Comment.objects.all().count()

  context = {
    'num_bloggers': num_bloggers,
    'num_blogposts': num_blogposts,
    'num_comments': num_comments,
  }
  return render(request, 'blog/index.html', context)


class BlogListView(generic.ListView):
  model = BlogPost
  paginate_by = 5


class BloggerListView(generic.ListView):
  model = Blogger


class BlogDetailView(generic.DetailView):
  model = BlogPost


class BloggerDetailView(generic.DetailView):
  model = Blogger


class CommentCreateView(LoginRequiredMixin, generic.CreateView):
  model = Comment
  fields = ['content']

  # runs on get
  def get_context_data(self, **kwargs: Any) -> Dict[str, Any]:
    context = super().get_context_data(**kwargs)
    context['blogpost'] = get_object_or_404(BlogPost, pk=self.kwargs['pk'])
    return context

  # runs on post
  def form_valid(self, form: BaseModelForm) -> HttpResponse:
    """Add author and associated blog to form data before setting it as valid (so it is saved to model)"""
    form.instance.author = self.request.user
    form.instance.blog = get_object_or_404(BlogPost, pk=self.kwargs['pk'])
    return super().form_valid(form)
