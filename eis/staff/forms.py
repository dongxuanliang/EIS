#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: dongxuanliang
@contact: dongxuanliang@maimiaotech.com
@date: 2014-10-17 14:45
@version: 0.0.0
@license: Copyright Maimiaotech.com
@copyright: Copyright Maimiaotech.com

"""
from django import forms

class StaffForm(forms.Form):
    name=forms.CharField()
    sex=forms.IntegerField()
    age=forms.IntegerField()
    workage=forms.IntegerField()
    edu=forms.CharField()
    salary=forms.IntegerField()
    address=forms.CharField()


