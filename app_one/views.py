from datetime import datetime

from django.http import HttpResponse
from django.shortcuts import redirect
from django.template.loader import get_template

from .models import Post


# Create your views here.
def homepage(request):
    template = get_template('app_one/index.html')
    posts = Post.objects.all()
    now = datetime.now()
    html = template.render(locals())
    return HttpResponse(html)

def showpost(request, slug):
    template = get_template('app_one/post.html')
    try:
        post = Post.objects.get(slug=slug)
        if post != None:
            html = template.render(locals())
            return HttpResponse(html)
    except:
        return redirect('/')