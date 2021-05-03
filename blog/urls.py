from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('owner/', views.get_OwnerForm, name='owner'),
    path('<owner_id>', views.owner_detail, name='owner_detail')
]
