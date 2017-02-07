# -*- coding: utf-8 -*-
__author__ = 'yuzhou'
__date__ = '2017/2/6 12:14'
from django.conf.urls import url, include

from .views import UserInfoView, UploadImageView, UpdataPwdView, \
    SendEmailCodeView, UpdateEmailView, MyCourseView, MyFavOrgView, \
    MyFavTeacherView, MyFavCourseView, MyMessageView


urlpatterns = [
    # 用户信息
    url(r'^info/$', UserInfoView.as_view(), name='user_info'),

    # 用户头像上传
    url(r'^image/$', UploadImageView.as_view(), name='image_upload'),

    # 用户个人中心修改密码
    url(r'^update/pwd/$', UpdataPwdView.as_view(), name='updatepwd'),

    # 发送验证码邮箱
    url(r'^sendemail_code/$', SendEmailCodeView.as_view(), name='sendemail_code'),

    # 发送验证码邮箱
    url(r'^update_email/$', UpdateEmailView.as_view(), name='update_email'),

    # 我的课程
    url(r'^mycourse/$', MyCourseView.as_view(), name='mycourse'),

    # 我收藏的课程机构
    url(r'^myfav/org/$', MyFavOrgView.as_view(), name='myfav_org'),

    # 我收藏的机构老师
    url(r'^myfav/teacher/$', MyFavTeacherView.as_view(), name='myfav_teacher'),

    # 我收藏的课程
    url(r'^myfav/course/$', MyFavCourseView.as_view(), name='myfav_course'),

    # 我的消息
    url(r'^myfav/message/$', MyMessageView.as_view(), name='mymessage'),

]