# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .models import Post
from django.views import generic

# Create your views here.
def index(request):
    num_posts = Post.objects.all().count()

#Render the HTML index.html
    return render(
        request,
        'index.html',
        context = {'num_posts':num_posts},
    )

class PostListView(generic.ListView):
    model = Post
    
