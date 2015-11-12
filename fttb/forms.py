# coding=UTF-8
from django import forms
from django.contrib.auth.models import User
from django.forms.widgets import RadioSelect
from datetime import date
from django.utils import safestring
from django.http import JsonResponse

class ipsearchForm(forms.Form):
    ip_search = forms.CharField()
