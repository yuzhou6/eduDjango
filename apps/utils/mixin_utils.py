# -*- coding: utf-8 -*-
__author__ = 'yuzhou'
__date__ = '2017/2/5 17:20'

from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

class LoginRequiredMixin(object):

    @method_decorator(login_required(login_url='/login/'))
    def dispath(self, request, *args, **kwargs):
        return super(LoginRequiredMixin, self).dispatch(request, *args, **kwargs)
