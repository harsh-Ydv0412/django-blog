from django.http import HttpResponse
from django.shortcuts import render

from assignment.models import About
from blogs.models import Blog, Category




def home(request):
  # cateogries = Category.objects.all()
  featured_post = Blog.objects.filter(is_featured = True, status= 'Published').order_by('updated_at')
  posts = Blog.objects.filter(is_featured= False, status= 'Published')
  # fetch about us
  try:
    about = About.objects.get()
  except:
    about = None

  context = {
    # 'cateogries' : cateogries,
    'featured_post' : featured_post,
    'posts' : posts,
    'about' : about,
  }
  return render(request, 'home.html', context) 