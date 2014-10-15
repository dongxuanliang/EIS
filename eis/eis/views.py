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

from django.http import HttpResponse

def hello(request):
    return HttpResponse("<html><body><p style='color:red'>Hello Word!</p></body></html>")
