# coding=UTF-8
from django.db import models
from simple_history.models import HistoricalRecords
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

class fttb_area(models.Model):
    area = models.CharField(max_length=10, default = '', verbose_name=u"區域")
    ip_range = models.CharField(max_length = 35, default = '', verbose_name = u"IP Range")
    subnet_mask = models.GenericIPAddressField(verbose_name=u"Subnet Mask")
    gateway = models.GenericIPAddressField(verbose_name = u"Gateway")
    dns = models.CharField(max_length = 35, default = '', verbose_name = u"DNS", blank=True)
    def __unicode__(self):
        return '%s %s'%(self.area, self.ip_range)

    class Meta:
        verbose_name_plural = (u"1. FTTB 區域範圍")


class fttb_iplist(models.Model):
    area = models.ForeignKey(fttb_area, verbose_name = u"區域")
    ip = models.GenericIPAddressField()
    applicant = models.CharField(max_length=30, verbose_name = u'申請人', default = '', blank = True)
    customer = models.CharField(max_length=30, verbose_name = u'客戶名稱', default = '', blank = True)
    ID_no = models.CharField(max_length=15, verbose_name = u'教職員編號/學號', default = '', blank = True)
    new_ID_no = models.CharField(max_length=15, verbose_name = u'碩(博)班新學號', default = '', blank = True)
    apply_type = models.CharField(max_length=25, verbose_name = u'申請型態', default = '', blank = True)
    attach_phone = models.CharField(max_length=15, verbose_name = u'附掛電話', default = '', blank = True)
    cellphone = models.CharField(max_length=12, verbose_name = u'手機', default = '', blank = True)
    phone_2 = models.CharField(max_length=18, verbose_name = u'聯絡電話2', default = '', blank = True)
    addr = models.CharField(max_length=50, verbose_name = u'裝機地址', default = '', blank = True)
    rate = models.CharField(max_length=15, verbose_name = u'速率', default = '', blank = True)
    apply_date = models.DateField(blank=True, verbose_name=u"申請日期", null=True)
    allotte_time = models.DateField(blank=True, verbose_name=u"分配日期", null=True)
    email = models.EmailField(verbose_name = u'E-mail', default = '', blank = True)
    circuit_no = models.CharField(max_length=10, verbose_name = u'電路編號', default = '', blank = True)
    completion_isnt = models.DateField(blank=True, verbose_name=u"是否竣工", null=True)
    notice = models.CharField(max_length=1, choices = (('Y', 'Yes'), ('N', 'No')), verbose_name = u'是否通知IP', default = 'N', blank = True)
    note = models.TextField(blank=True, default='', max_length=500, verbose_name=u"備註")
    history = HistoricalRecords()
   
    def __unicode__(self):
        return '%s'%(self.ip)

    class Meta:
        verbose_name_plural = (u"2. FTTB IP 列表")


