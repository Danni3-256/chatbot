from .models import Destination 
from .models import Accommodation 
from .models import Activity 

from django.contrib import admin

admin.site.register(Destination)
admin.site.register(Accommodation)
admin.site.register(Activity)