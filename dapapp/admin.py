from django.contrib import admin
from .models import County, Subcounty, DeliveriesInfo, MaternalDeathsInfo

admin.site.site_header = 'Project Admin Center'

# Register your models here.
class countyAdmin(admin.ModelAdmin):
	list_display = ['countyname', 'code']

class subcountyAdmin(admin.ModelAdmin):
	list_display = ['county', 'subcountyname']

class deliveriesAdmin(admin.ModelAdmin):
	list_display = ['facilityname', 'subcountyname','dateentered']

admin.site.register(County, countyAdmin)
admin.site.register(Subcounty, subcountyAdmin)
admin.site.register(DeliveriesInfo, deliveriesAdmin)
admin.site.register(MaternalDeathsInfo)
		