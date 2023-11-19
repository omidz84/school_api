from rest_framework.permissions import BasePermission, DjangoModelPermissions


class IsOwner(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(request.user == obj.class_id.teacher)


class IsUser(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(request.user == obj)


class IsTeacher(BasePermission):

    def has_object_permission(self, request, view, obj):
        return bool(request.user == obj.teacher)


class CustomModelPermissions(DjangoModelPermissions):
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'],
        'OPTIONS': ['%(app_label)s.view_%(model_name)s'],
        'HEAD': ['%(app_label)s.view_%(model_name)s'],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
