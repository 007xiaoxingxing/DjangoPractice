# -*- coding:utf-8 -*-
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    定制权限，只允许拥有者去编辑snippet
    """

    def has_object_permission(self, request, view, obj):
        # 所有人拥有读取权限
        # 允许GET POST  OPTIONS请求
        if request.method in permissions.SAFE_METHODS:
            return True

        # 写权限只给snippet的拥有者
        return obj.owner == request.user
