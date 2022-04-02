from datetime import datetime

import markdown
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template

from .models import Post


# Create your views here.
def homepage(request):
    template = get_template('app_one/index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)


def showpost(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.body = markdown.markdown(post.body,
                                  extensions=[
                                      'markdown.extensions.extra',  # 標題、表格、引用等基本轉換
                                      'markdown.extensions.codehilite',  # 語法 highlight
                                      'markdown.extensions.toc',  # 生成目錄
                                  ])
    return render(request, 'app_one/post.html', context={'post': post})
