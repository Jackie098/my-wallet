from django.contrib import admin

from .models import Investor,Operation

# Register your models here.
admin.site.register(Investor)
admin.site.register(Operation)