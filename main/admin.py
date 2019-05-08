from django.contrib import admin
from main.models import IPAddr

# Register your models here.

class IPAddrAdmin(admin.ModelAdmin):
  list_display = ['ip', 'visitCount', 'visitTime']

admin.site.register(IPAddr, IPAddrAdmin)