# coding=UTF-8
from django.contrib import admin
from models import *
from simple_history.admin import SimpleHistoryAdmin
#from django.template import Template

class fttb_areaAdmin(admin.ModelAdmin):
    list_display = ('id', 'area', 'ip_range', 'subnet_mask', 'gateway', 'dns')
    def get_ordering(self, request):
        return ['area']
admin.site.register(fttb_area, fttb_areaAdmin)




#class fttb_iplistAdmin(admin.ModelAdmin):
class fttb_iplistAdmin(SimpleHistoryAdmin):
#    change_history_template ='admin/fttb_list/fttb_iplist/object_history.html'
    list_display = ('id', 'ip', 'applicant', 'customer', 'ID_no', 'attach_phone', 'cellphone', 'rate', 'apply_date', 'allotte_time', 'email', 'circuit_no', 'completion_isnt', 'notice')
    list_filter = ['area']
    search_fields = ('ip',)

    def get_ordering(self, request):
        return ['id']
#admin.site.register(fttb_iplist, fttb_iplistAdmin)
admin.site.register(fttb_iplist, fttb_iplistAdmin)


