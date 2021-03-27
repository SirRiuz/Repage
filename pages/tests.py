

from django.test import TestCase
import uuid
from .models import Page


page = Page.objects.get(name='faztpage').delete()
