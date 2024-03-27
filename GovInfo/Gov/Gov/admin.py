from django.contrib import admin
from .models import Gov
from parliament.models import MemberOfParliament
from senate.models import Senators
from Governor.models import Governors
from county.models import MCA


admin.site.register(Gov)
admin.site.register(MemberOfParliament)
admin.site.register(Senators)
admin.site.register(Governors)
admin.site.register(MCA)
