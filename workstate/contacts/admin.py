from django.contrib import admin

# Register your models here.
from .models import Contact,Person,Solution

admin.site.register(Person)
admin.site.register(Contact)
admin.site.register(Solution)
