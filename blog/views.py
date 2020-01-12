from django.views.generic import ListView, CreateView 
from django.urls import reverse_lazy 
from django.db.models import Q
from .forms import PostForm 
from .models import Post

class HomePageView(ListView):
    model = Post
    template_name = 'home.html'

class CreatePostView(CreateView): 
    model = Post
    form_class = PostForm
    template_name = 'post.html'
    success_url = reverse_lazy('home')


    def get_blog_(query=None):
    	queryset = []
    	queries = query.split(" ")
    	for q in queries:
    		posts = blog.object.filter(
    			Q(title__iconstrains=q)
    			Q(body__iconstrains=q)
    			).distinct()

    		for post in post:
    			queryset.append(post)

    			return list(set(queryset))