# coding=UTF-8
import _mysql, MySQLdb, string
from django.shortcuts import render_to_response,render,get_object_or_404
from django.core.urlresolvers import reverse
from django.http import Http404, HttpResponseRedirect, HttpResponse, Http404
from django import forms
from django.contrib.auth.models import User
from django.contrib import auth
from django.contrib import messages
from django.template.context import RequestContext
from .forms import ipsearchForm
from . import forms
from fttb_list.models import *
import json
#import simplejson
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def index(request):
    if request.method == 'POST' :
        form = ipsearchForm(request.POST)
        if form.is_valid():
            ip_search = form.cleaned_data["ip_search"]
            request.session['ip_search'] = ip_search
            show_ip = fttb_iplist.objects.filter(ip=ip_search).values_list('ip', 'customer') 
            print show_ip[0]
            return render_to_response('fttb/index.html', RequestContext(request, locals()))
    else:
        form = ipsearchForm()
        return render_to_response('fttb/index.html', RequestContext(request, locals()))
    return render_to_response('fttb/index.html', RequestContext(request, locals()))

