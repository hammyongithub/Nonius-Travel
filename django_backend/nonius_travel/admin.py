from django.contrib import admin
from .models import *

class ContactInline(admin.TabularInline):
    model = Contact 
class DocumentInline(admin.TabularInline):
    model = Document
class AddressInline(admin.TabularInline):
    model = Address
class ReservationsInline(admin.TabularInline):
    model = Reservations
class ClientsAdmin(admin.ModelAdmin):
    inlines = [ContactInline, DocumentInline, AddressInline, ReservationsInline]
    list_display = ('name', 'birthdate', 'created_at')
    prepopulated_fields = {'slug': ('name',)}



admin.site.register(Clients, ClientsAdmin)
admin.site.register(Document)
admin.site.register(Contact)
admin.site.register(Address)
admin.site.register(Reservations)
admin.site.register(Guests)
admin.site.register(Payment)
admin.site.register(Card)