from django.contrib import admin
from .models import Gov
from ..parliament.models import parliament

admin.site.register(Gov)
admin.site.register(parliament)
