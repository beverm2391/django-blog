from django.shortcuts import render

from django.views import View, generic
from django.views.generic import TemplateView
from .models import Post
from django.http import HttpResponse

#!! create a new view for index so that I can use the current "index" view for the blog page I created

class AboutMePageView(TemplateView):
    template_name = 'about-me.html'

class HomePageView(TemplateView):
    template_name = 'index.html'

class PostList(generic.ListView):
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'blog.html'

class PostDetail(generic.DetailView):
    model = Post
    template_name = 'post_detail.html'
