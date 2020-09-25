from django.shortcuts import render
from django.views.generic import ListView , DetailView
from . models import Post


# Create your views here.

posts = [
    {
        'author': 'CoreyMS',
        'title': 'Blog Post 1',
        'content': 'First post content',
        'date_posted': 'August 27, 2018'
    },
    {
        'author': 'Jane Doe',
        'title': 'Blog Post 2',
        'content': 'Second post content',
        'date_posted': 'August 28, 2018'
    }
]
def home (request):
   context={'posts':posts}

   return render(request,'blog/home.html',context)

class PostListView (ListView):
    model = Post
    template_name ='blog/home.html'
    context_object_name = 'posts'
    ordering = ['-date_posted']
    
class PostDetailView (DetailView):
    model = Post


def about(request):
     return render(request, 'blog/about.html', {'title': 'About'}) 