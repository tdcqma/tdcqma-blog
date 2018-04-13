from django.shortcuts import render
from .models import BLogArticles

def blog_title(request):
    blogs = BLogArticles.objects.all()
    return render(request,"blog/titles.html",{"blogs":blogs})