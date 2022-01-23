from django.urls import  path
from . import views

# app_name = 'blog'
urlpatterns = [
    path('owner_list/', views.OwnerListView.as_view(), name='owner_list'),
    path('owner_list/<int:pk>/', views.OwnerDetailView.as_view(), name='owner_detail'),
    path('pet_list/', views.PetListView.as_view(), name='pet_list'),
    path('pet_list/<int:pk>/', views.PetDetailView.as_view(), name='pet_detail'),
    path('pet_create/', views.PetCreateView.as_view(), name='pet_create'),
    path('pet_list/<int:pk>/update', views.PetUpdateView.as_view(), name='pet_update'),
    path('pet_list/<int:pk>/delete', views.PetDeleteView.as_view(),  name='pet_delete'),
    path('userHomepage/', views.UserHomepageTemplateView.as_view(), name='userHomepage')


    # path('owner/', views.get_OwnerForm, name='owner'),
    # path('<owner_id>', views.owner_detail, name='owner_detail')
]
