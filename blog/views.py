from django.shortcuts import render , get_object_or_404
from .forms import OwnerForm
from django.http import HttpResponseRedirect
import datetime
from django.utils.timezone import now
from .models import Owner
from .models import Author

# Create your views here.
def owner_detail(request, owner_id):
    owner = get_object_or_404(Owner, pk=owner_id)
    return render(request, 'owner_detail.html', {'owner': owner})

def get_OwnerForm(request):
    form = OwnerForm()
    if request.method == 'POST':
        form = OwnerForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return HttpResponseRedirect('/')
        else:
            print('error form validation')

    return render(request, 'owner.html', {'form': form})


def index(request):
    owners_list = Owner.objects.all()
    return render(request, 'index.html', {'owners_list': owners_list})



def homepage(request):
    # html = "<html><body>it is now : %s .<html><body>" % now()
    return render(request, 'homepage.html', {'current_time': now()})
