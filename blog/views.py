from django.shortcuts import render
from .models import Author

# Create your views here.
def index(request):
    authors_list= Author.objects.all()
    return render(request,'index.html',{'authors_list':authors_list})
    #return render(request,'index.html')