from django.http import HttpResponse
from django.template.loader import get_template

from app_two import models


# Create your views here.
def index(request):
    products = models.Product.objects.all()
    template = get_template('app_two/index.html')
    html = template.render(locals())
    return HttpResponse(html)


def detail(request, id):
    try:
        product = models.Product.objects.get(id=id)
        images = models.PPhoto.objects.filter(product=product)
    except:
        pass
    template = get_template('app_two/detail.html')
    html = template.render(locals())
    return HttpResponse(html)