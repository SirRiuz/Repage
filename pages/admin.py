
# Django
from django.contrib import admin


# Models
from .models import Page



@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass
