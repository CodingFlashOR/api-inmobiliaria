from rest_framework.permissions import BasePermission
from rest_framework.generics import GenericAPIView
from rest_framework.request import Request


class SwaggerUIPublic(BasePermission):
    """
    Permission class to allow access to the Swagger UI.
    """

    message = "This is a public Swagger interface, you do not have permission to use this endpoint."

    def has_permission(self, request: Request, view: GenericAPIView) -> bool:
        return False
