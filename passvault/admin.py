from django.contrib import admin

# register your models here.

from .models import User,SavedPassword

admin.site.register(User)
admin.site.register(SavedPassword)
