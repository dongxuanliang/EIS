#! /usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author: dongxuanliang
@contact: dongxuanliang@maimiaotech.com
@date: 2014-10-15 17:09
@version: 0.0.0
@license: Copyright Maimiaotech.com
@copyright: Copyright Maimiaotech.com

"""
import logging

logger = logging.getLogger()

def log_record(step=1):
    def _wrapper_func(func):
        def __wrapped_func(*args, **kwargs):
            res = None
            logger.info("start the function:"+func.__name__)
            res =  func(*args, **kwargs)
            logger.info("finish the function:"+func.__name__)
            return res
        return __wrapped_func
    return _wrapper_func

def log_test(func):
    def wrapper_func(*args, **kwargs):
        res = None
        logger.info("start the function:"+func.__name__)
        res = func(*args, **kwargs)
        logger.info("finish the function:"+func.__name__)
        return res
    return wrapper_func
