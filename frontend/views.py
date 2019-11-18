from django.shortcuts import render
from django.conf import settings


def html1(request):
    href = f'https://{settings.ALLOWED_HOSTS[0]}/dop/'
    return render(request, 'frontend/index.html', locals())


def html2(request):

    return render(request, 'frontend/index2.html', locals())
# Create your views here.
