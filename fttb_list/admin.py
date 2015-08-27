# coding=UTF-8
from django.contrib import admin
from models import *
from simple_history.admin import SimpleHistoryAdmin
#from django.template import Template

admin.site.disable_action('delete_selected')


class fttb_areaAdmin(admin.ModelAdmin):
    list_display = ('id', 'area', 'ip_range', 'subnet_mask', 'gateway', 'dns')
    def get_ordering(self, request):
        return ['area']
admin.site.register(fttb_area, fttb_areaAdmin)



def make_clear(self, request, queryset):
    queryset.update(applicant='', customer='', ID_no='', new_ID_no='', apply_type='', attach_phone='', cellphone='', phone_2='', addr='', rate='', apply_date=None, allotte_time=None, email='', circuit_no='', completion_isnt=None, notice='N', note='')
make_clear.short_description = "Mark selected IP as clear"



#class fttb_iplistAdmin(admin.ModelAdmin):
class fttb_iplistAdmin(SimpleHistoryAdmin):
    #change_form_template = 'admin/fttp_iplist/extras/fttb_iplist_change_form.html'
    list_display = ('id', 'ip', 'applicant', 'customer', 'ID_no', 'cellphone', 'phone_2', 'rate', 'apply_date', 'email', 'addr', 'circuit_no', 'note', 'get_mask', 'get_gateway')
    list_display_links = ['id','ip']
    list_filter = ['area']
    search_fields = ('ip','applicant', 'customer', 'attach_phone', 'ID_no')
    actions = [make_clear]

    def get_mask(self, obj):
        return obj.area.subnet_mask
    get_mask.short_description='子網路遮罩'

    def get_gateway(self, obj):
        return obj.area.gateway
    get_gateway.short_description='預設閘道'


    def get_ordering(self, request):
        return ['id']

    def has_delete_permission(self, request, *args):
        return False

#    def has_delete_permission(self, request, *args):
#        self.update(applicant='', customer='', ID_no='', new_ID_no='', apply_type='', attach_phone='', cellphone='', phone_2='', addr='', rate='', apply_date=None, allotte_time=None, email='', circuit_no='', completion_isnt=None, notice='N', note='')
#        return True 
    #has_delete_permission.short_description = "資料清除"

#admin.site.register(fttb_iplist, fttb_iplistAdmin)
admin.site.register(fttb_iplist, fttb_iplistAdmin)


