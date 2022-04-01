from datetime import datetime

from django.http import HttpResponse
from django.template.loader import get_template


# Create your views here.
def main_page(request):
    template = get_template('app_/main.html')
    now = datetime.now()
    html = template.render(locals())  # get all local args into dict
    return HttpResponse(html)