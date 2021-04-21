from django.contrib import admin
from .models import Post, Author

# Register your models here.
class AuthorAdmin(admin.ModelAdmin):
    fields = ((('name','first_name'),'date_of_birth'))

admin.site.register(Author, AuthorAdmin)
admin.site.register(Post)

