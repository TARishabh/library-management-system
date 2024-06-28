# from rest_framework import permissions

# class IsLibrarianOrReadOnly(permissions.BasePermission):
#     """
#     Permission class to allow only librarians to create, update, and delete users.
#     """
#     pass
#     # def has_permission(self, request, view):
#     #     if request.method in permissions.SAFE_METHODS:  
#     #         return True
#     #     return request.user.is_authenticated and request.user.role == 'librarian'