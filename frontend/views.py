from django.shortcuts import render
from django.conf import settings
from .forms import SubscribeForm
from .models import Subscribers
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt


@csrf_exempt
def landing(request, email_we_check=None):
    form = SubscribeForm(request.POST or None)

    if request.method == "POST" and form.is_valid():
        form = form.save()
        return render(request, 'frontend/index2.html', locals())
    return render(request, 'frontend/index.html', locals())
# Create your views here.
