from django.contrib import admin
from .models import *

# Register your models here.
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'date_in', 'date_out')
    search_fields = ('name', 'phone', 'room')
    ordering = ['-date_in']


admin.site.register(Room)
admin.site.register(TypeRoom)
admin.site.register(Booking, BookingAdmin)
