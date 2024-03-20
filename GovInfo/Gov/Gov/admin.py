from django.contrib import admin
from .models import Gov
from parliament.models import MemberOfParliament


admin.site.register(Gov)
admin.site.register(MemberOfParliament)
