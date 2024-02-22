from rest_framework.permissions import BasePermission

class IsUploaderPermission(BasePermission):
    """
    Permission check if user is uploader or not
    """

    def has_permission(self, request, view):

        if request.user.is_authenticated:
            return request.user.is_uploader
        return False
    
class IsMangaOwnerPermission(BasePermission):
    """
    Permission check if user is owner of manga
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return obj.owner == request.user
        return False

class IsChapterOwnerPermission(BasePermission):
    """
    Permission check if user is owner of chapter
    """

    def has_object_permission(self, request, view, obj):
        if request.user.is_authenticated:
            return obj.manga.owner == request.user
        return False