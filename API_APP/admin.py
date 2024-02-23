from django.contrib import admin
from .models import Profile

admin.site.register(Profile)
# class AuthorAdmin(admin.ModelAdmin):
#   list_display = ['username','email','password','gender','city','skill']
