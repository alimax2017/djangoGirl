from django.contrib import admin
from .models import Race, Owner, Vaccine, Pet
from .forms import OwnerForm

# Register your models here.
class OwnerAdmin(admin.ModelAdmin):
    list_display = ('last_name','first_name')

admin.site.register(Owner, OwnerAdmin)

admin.site.register(Race)
admin.site.register(Pet)
admin.site.register(Vaccine)


