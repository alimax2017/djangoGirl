from django.shortcuts import render
from django.http import HttpResponse
import datetime
from django.utils.timezone import now
from .models import Author


# Create your views here.
def index(request):
    authors_list = Author.objects.all()
    return render(request, 'index.html', {'authors_list': authors_list})
    # return render(request,'index.html')


def homepage(request):
    # html = "<html><body>it is now : %s .<html><body>" % now()
    return render(request, 'homepage.html', {'current_time' : now()})
