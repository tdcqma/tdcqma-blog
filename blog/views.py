from django.shortcuts import render,get_object_or_404
from .models import BlogArticles

# 显示文章列表
def blog_title(request):
    blogs = BlogArticles.objects.all()
    return render(request,"blog/titles.html",{"blogs":blogs})

# 显示文章详情
def blog_article(request,article_id):
    #article = BlogArticles.objects.get(id=article_id)   # 如果article_id不存在会报错
    article = get_object_or_404(BlogArticles,id=article_id)
    pub = article.publish
    return render(request,"blog/content.html",{"article":article,"publish":pub})