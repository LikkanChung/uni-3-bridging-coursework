from django.shortcuts import render
from django.utils import timezone
from blog.models import Post
from cv.models import Education, Experience, Volunteering
from portfolio.models import Project

# Create your views here.
def home(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'home/home.html', {'posts': posts})
