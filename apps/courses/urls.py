# -*- coding: utf-8 -*-
__author__ = 'yuzhou'
__date__ = '2017/2/4 0:04'

from django.conf.urls import url, include
from courses.views import CourseListView, CourseDetailView, CourseInfoView, CommentsView, AddCommentsView, VideoDisplayView

urlpatterns = [
    # 课程列表页
    url(r'^list/$', CourseListView.as_view(), name='course_list'),

    # 课程列表页
    url(r'^detail/(?P<course_id>\d+)/$', CourseDetailView.as_view(), name='course_detail'),

    # 课程详情信息
    url(r'^info/(?P<course_id>\d+)/$', CourseInfoView.as_view(), name='course_info'),

    # 课程评论
    url(r'^comment/(?P<course_id>\d+)/$', CommentsView.as_view(), name='course_comments'),

    # 添加课程评论
    url(r'^add_comment/$', AddCommentsView.as_view(), name='add_comments'),

    # 添加课程评论
    # url(r'^add_comment/$', AddCommentsView.as_view(), name='add_comments'),

    # 访问视频地址
    url(r'^video/(?P<video_id>\d+)/$', VideoDisplayView.as_view(), name='video_play'),

]
