from rest_framework.permissions import BasePermission


class ImagePermissions(BasePermission):

    def has_permission(self, request, view):
        user = request.user

        if view.action in ["destroy", "create", "update"] and user:
            return True
        return view.action in ["list", "retrieve"]

    def has_object_permission(self, request, view, obj):
        user = request.user

        return obj.user == user

