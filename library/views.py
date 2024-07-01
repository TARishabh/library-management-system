from rest_framework import status, permissions,viewsets
from rest_framework.mixins import ListModelMixin, CreateModelMixin, RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin
from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from .serializers import UserSerializer, AuthorSerializer, BookSerializer, IssuedBookSerializer
from .pagination import TaskPagination
from .models import User, Author, Book, IssuedBook
from .renderers import CustomRenderer

'''The Flow of this v4 is also explained in the README.md file'''
class UserViewSet(
    ListModelMixin, CreateModelMixin, RetrieveModelMixin,
    UpdateModelMixin, DestroyModelMixin, viewsets.GenericViewSet
):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    pagination_class = TaskPagination
    permission_classes = [permissions.AllowAny]
    renderer_classes = [CustomRenderer]

    response_data = {
        "list": {
            "message": "List of user records",
            "status_code": status.HTTP_200_OK
        },
        "retrieve": {
            "message": "Requested user record retrieved",
            "status_code": status.HTTP_200_OK
        },
        "partial_update": {
            "message": "Requested user record updated",
            "status_code": status.HTTP_202_ACCEPTED
        },
        "destroy": {
            "message": "Requested user record deleted",
            "status_code": status.HTTP_204_NO_CONTENT
        },
        "create": {
            "message": "New user record created",
            "status_code": status.HTTP_201_CREATED
        }
    }

    def get_queryset(self):
        return super().get_queryset()

    def get_object(self):
        return super().get_object()

    def get_serializer_class(self):
        return super().get_serializer_class()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def get_renderer_context(self):
        context = super().get_renderer_context()
        if self.action in self.response_data:
            context["message"] = (
                self.response_data.get(self.action).get("message")
            )
            context["status_code"] = (
                self.response_data.get(self.action).get("status_code")
            )
        return context

class AuthorViewSet(
    ListModelMixin, CreateModelMixin, RetrieveModelMixin,
    UpdateModelMixin, DestroyModelMixin, viewsets.GenericViewSet
):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer
    permission_classes = [permissions.AllowAny]
    renderer_classes = [CustomRenderer]

    response_data = {
        "list": {
            "message": "List of author records",
            "status_code": status.HTTP_200_OK
        },
        "retrieve": {
            "message": "Requested author record retrieved",
            "status_code": status.HTTP_200_OK
        },
        "partial_update": {
            "message": "Requested author record updated",
            "status_code": status.HTTP_202_ACCEPTED
        },
        "destroy": {
            "message": "Requested author record deleted",
            "status_code": status.HTTP_204_NO_CONTENT
        },
        "create": {
            "message": "New author record created",
            "status_code": status.HTTP_201_CREATED
        }
    }

    def get_queryset(self):
        return super().get_queryset()

    def get_object(self):
        return super().get_object()

    def get_serializer_class(self):
        return super().get_serializer_class()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context

    def get_renderer_context(self):
        context = super().get_renderer_context()
        if self.action in self.response_data:
            context["message"] = (
                self.response_data.get(self.action).get("message")
            )
            context["status_code"] = (
                self.response_data.get(self.action).get("status_code")
            )
        return context

class BookViewSet(
    ListModelMixin, CreateModelMixin, RetrieveModelMixin,
    UpdateModelMixin, DestroyModelMixin, viewsets.GenericViewSet
):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]
    renderer_classes = [CustomRenderer]

    response_data = {
        "list": {
            "message": "List of book records",
            "status_code": status.HTTP_200_OK
        },
        "retrieve": {
            "message": "Requested book record retrieved",
            "status_code": status.HTTP_200_OK
        },
        "partial_update": {
            "message": "Requested book record updated",
            "status_code": status.HTTP_202_ACCEPTED
        },
        "destroy": {
            "message": "Requested book record deleted",
            "status_code": status.HTTP_204_NO_CONTENT
        },
        "create": {
            "message": "New book record created",
            "status_code": status.HTTP_201_CREATED
        }
    }

    def get_queryset(self):
        return super().get_queryset()

    def get_object(self):
        return super().get_object()

    def get_serializer_class(self):
        return super().get_serializer_class()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
    def get_renderer_context(self):
        context = super().get_renderer_context()
        if self.action in self.response_data:
            context["message"] = (
                self.response_data.get(self.action).get("message")
            )
            context["status_code"] = (
                self.response_data.get(self.action).get("status_code")
            )
        return context
class IssuedBookViewSet(
    ListModelMixin, CreateModelMixin, RetrieveModelMixin,
    UpdateModelMixin, DestroyModelMixin, viewsets.GenericViewSet
):
    queryset = IssuedBook.objects.all()
    serializer_class = IssuedBookSerializer
    permission_classes = [permissions.AllowAny]
    renderer_classes = [CustomRenderer]

    response_data = {
        "list": {
            "message": "List of issued book records",
            "status_code": status.HTTP_200_OK
        },
        "retrieve": {
            "message": "Requested issued book record retrieved",
            "status_code": status.HTTP_200_OK
        },
        "partial_update": {
            "message": "Requested issued book record updated",
            "status_code": status.HTTP_202_ACCEPTED
        },
        "destroy": {
            "message": "Requested issued book record deleted",
            "status_code": status.HTTP_204_NO_CONTENT
        },
        "create": {
            "message": "New issued book record created",
            "status_code": status.HTTP_201_CREATED
        }
    }

    def get_queryset(self):
        return super().get_queryset()

    def get_object(self):
        return super().get_object()

    def get_serializer_class(self):
        return super().get_serializer_class()

    def get_serializer_context(self):
        context = super().get_serializer_context()
        context.update({"request": self.request})
        return context
    
    def get_renderer_context(self):
        context = super().get_renderer_context()
        if self.action in self.response_data:
            context["message"] = (
                self.response_data.get(self.action).get("message")
            )
            context["status_code"] = (
                self.response_data.get(self.action).get("status_code")
            )
        return context