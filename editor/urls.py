# -*- coding: utf-8 -*-
# @Author: AndersonHJB
# @Date:   2019-04-25 00:30:09
# @Last Modified by:   aiyuechuang
# @Last Modified time: 2021-02-23 14:21:34
from django.urls import path

from . import views

urlpatterns = [
    path("", views.editor, name="editor"),
    path("upload_code", views.upload_code, name="upload_code")
]
