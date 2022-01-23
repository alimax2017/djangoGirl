from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, redirect, HttpResponseRedirect
from django.views.generic import (TemplateView, ListView, DetailView,
                                  CreateView, UpdateView, DeleteView)
from .forms import OwnerForm, PetForm, IDForm
from django.http import HttpResponseRedirect
from .models import Owner, Pet
import datetime

class UserHomepageTemplateView(TemplateView):
    template_name = 'blog/userHomepage.html'

def loginpage(request):
    return render(request, 'registration/login.html')

def signuppage(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('homepage')
    else:
        form = UserCreationForm()
    return render(request, 'registration/signup.html', {'form': form})

def homepage(request):
    if request.method == 'POST':
        form = IDForm(request.POST) #IDForm est un formulaire où le site demande à l'utilisateur l'ID de son pet
        if form.is_valid():
            pet_ID=form.cleaned_data['ID_number']
            return HttpResponseRedirect(reverse('blog:pet_detail', args=(pet_ID,)) ) #retoure à la page de detail du pet dont le ID aété entré dans le formulaire
    else:
        form = IDForm()

    return render(request, 'homepage.html', {'form':form})

#The old way to do it
# def homepage(request):
#     # html = "<html><body>it is now : %s .<html><body>" % now()
#     return render(request, 'homepage.html', {'current_time': now()})

class OwnerListView(ListView): #affiche la page html correspondante nommée owner_list
    model = Owner
    context_object_name = 'owners'  #by default it is owner_list

class OwnerDetailView(DetailView): #affiche la page html owner_detail
    model = Owner
    #by default returns owner but if you want to change it use:
    #context_object_name = 'koukou'
    template_view = 'blog/owner_detail.html'
    context_object_name = 'this_owner'  #by default owner

class PetListView(ListView): #affiche pet_list.html
    #crée la variable pet_list liste des pet (dont le modele est appelé ci-après)
    model = Pet
# def owner_detail(request, owner_id):
#     owner = get_object_or_404(Owner, pk=owner_id)
#     return render(request, 'owner_detail.html', {'owner': owner})
class PetDetailView(DetailView): #lui correspond la page html: pet_detail.html
    model = Pet

class PetCreateView(CreateView): #lui correspond lapage html : pet_create.html (automatiquement créee sur la base du modele pet)
    model = Pet
    fields = ('name', 'race', 'owner')
    success_url = reverse_lazy('blog:pet_list') #page vers laquelle le site retourne une fois l'action de création terminée

class PetUpdateView(UpdateView): #lui correspond la page pet_update.html
    model = Pet
    fields = ('name', 'owner')
    success_url = reverse_lazy('blog:pet_list') #revenir sur la page pet_list une fois que la suppression est faite
#remarque: pet_create.html ,pet_delete.html et pet_update.html ne figurent pas dans le dossier temlate (inclus dnas le process)
class PetDeleteView(DeleteView): #lui correspond lapage pet_delete.html
    model = Pet
    success_url = reverse_lazy('blog:pet_list') #revenir sur la page pet_list une fois que la suppression est faite

#
# def get_pet(request):
#     form = PetForm()
#     if request.method == 'POST':
#         form = PetForm(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             return HttpResponseRedirect('/')
#     return render(request, 'pet.html', {'form':form})
#
# def get_OwnerForm(request):
#     form = OwnerForm()
#     if request.method == 'POST':
#         form = OwnerForm(request.POST)
#         if form.is_valid():
#             form.save(commit=True)
#             return HttpResponseRedirect('/')
#         else:
#             print('error form validation')
#
#     return render(request, 'owner.html', {'form': form})
#





