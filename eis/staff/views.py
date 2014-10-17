#! /usr/bin/env python
# -*- coding: utf-8 -*-

from django.shortcuts import render_to_response,RequestContext,HttpResponseRedirect
from django.contrib import auth
from django.utils import simplejson
from django.http import HttpResponse
from staff.models import Staff
from django.core import serializers
from django.core.paginator import Paginator,PageNotAnInteger,EmptyPage
from staff.forms import StaffForm
from django.contrib.auth.decorators import login_required

def login_view(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            data={'success':'true','msg':'/main/'}
        else:
            data={'success':'false','msg':'用户名或者密码错误'}
        return HttpResponse(simplejson.dumps(data, ensure_ascii=False))
    else:
        return render_to_response('login.html',context_instance=RequestContext(request))

@login_required
def main(request):
    return  render_to_response('main.html',context_instance=RequestContext(request))

@login_required
def logout_view(request):
    auth.logout(request)
    return HttpResponseRedirect('/accounts/login/')

@login_required
def ajax_staff_list(request):
    callback = request.GET.get('callback','null')
    name = request.GET.get('name','')
    page = request.GET.get('page',1)
    limit = request.GET.get('limit',25)
    queryset = Staff.objects.filter(name__contains=name)
    paginator = Paginator(queryset, limit)
    try:
        staffs = paginator.page(page)
    except PageNotAnInteger:
        staffs = paginator.page(1)
    except EmptyPage:
        staffs = paginator.page(paginator.num_pages)
    data = '%s({"total": %s, "%s": %s})' %(callback, queryset.count(), 'records', serializers.serialize('json', staffs))
    return HttpResponse(data)

@login_required
def ajax_staff_del(request):
    ids = request.GET.get('ids','');
    try:
        Staff.objects.extra(where=['id IN ('+ ids+')']).delete()
        data={'success':'true'}
    except Exception:
        data={'success':'false','msg':'系统异常'}
    return HttpResponse(simplejson.dumps(data, ensure_ascii=False))

@login_required
def ajax_staff_add(request):
    form = StaffForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        age = form.cleaned_data['age']
        sex = form.cleaned_data['sex']
        workage = form.cleaned_data['workage']
        edu = form.cleaned_data['edu']
        salary = form.cleaned_data['salary']
        address = form.cleaned_data['address']
        staff = Staff(name=name,age=age,sex=sex,workage=workage,edu=edu,salary=salary,address=address)
        staff.save()
        data={'success':'true'}
    else:
        data={'success':'false','msg':'添加数据失败'}
    return HttpResponse(simplejson.dumps(data, ensure_ascii=False))


