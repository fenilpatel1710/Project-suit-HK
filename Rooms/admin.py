from django.contrib import admin
from. models import room
from. models import roomfloor
from. models import roomtype
from.models import roomstatus
# from.models import detaillists

# Register your models here.
 
admin.site.register(room)
admin.site.register(roomfloor)
admin.site.register(roomtype)
admin.site.register(roomstatus)
# admin.site.register(detaillists)


