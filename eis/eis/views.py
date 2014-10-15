#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: dongxuanliang
@contact: dongxuanliang@maimiaotech.com
@date: 2014-10-15 13:49
@version: 0.0.0
@license: Copyright Maimiaotech.com
@copyright: Copyright Maimiaotech.com

"""
from django.template.loader import get_template
from django.template import Context
from django.http import HttpResponse

def hello(request,param):
    t = get_template('hello.html')
    html = t.render(Context({'param': param}))
    return HttpResponse(html)

def hello2(request):
    return HttpResponse("<html><body><p style='color:red'>Hello Word!</p></body></html>")
