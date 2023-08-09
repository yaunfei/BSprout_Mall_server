from django.contrib import admin
from .models import SpuInfo


# Register your models here.
class MerchandiseAdmin(admin.ModelAdmin):

    # list_display = ('name', 'amount', 'main_url')
    pass


admin.site.register(SpuInfo, MerchandiseAdmin)
