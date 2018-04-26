from django.contrib import admin
from .models import Character, Poll, Choice

# Register your models here.

admin.site.register(Character)
admin.site.register(Poll)
admin.site.register(Choice)

