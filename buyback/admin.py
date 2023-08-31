from datetime import datetime
from django.contrib import admin
from .models import Companie, Client

admin.site.site_header = 'LakshmiShree Administration'

admin.site.site_title = 'LakshmiShree Site Admin'

# Register your models here.
# admin.site.register(Companie)
# admin.site.register(Client)
from django.contrib.auth.models import Group
admin.site.unregister(Group)


from rangefilter.filters import DateRangeFilterBuilder, DateTimeRangeFilterBuilder, NumericRangeFilterBuilder

from import_export.admin import ImportExportMixin

class Clients(ImportExportMixin, admin.ModelAdmin):
     list_filter = (
        ("adate", DateRangeFilterBuilder()),
        ("status"),
    )
     list_display = ['ccode', 'cname', 'pan', 'dac', 'mobile', 'symbol', 'qty', 'status', 'adate']

admin.site.register(Client, Clients)

class Companies(ImportExportMixin, admin.ModelAdmin):
    list_display = ['symbol', 'name', 'logo', 'odate', 'cdate', 'price', 'size']
    # actions = ['upload_client_data']
    # class Meta:
    #     model = Companie
    #     fields =
    # def create_company_with_client(modeladmin, request, queryset):
    #     # Create employees associated with the new company
    #     for client_data in queryset:
    #         Client.objects.create(ccode = client_data.ccode,
    #                           cname = client_data.cname,
    #                           pan = client_data.pan,
    #                           dac = client_data.dac,
    #                           mobile = client_data.mobile,
    #                           qty = client_data.qty,
    #                           )

admin.site.register(Companie, Companies)






 
 




