"""
Views for the recipe APIs.

This module contains the views for handling recipe-related API requests.
It includes functionalities for creating, retrieving, updating, and deleting recipes.
The views interact with the Recipe model and utilize serializers to convert
model instances to JSON format and vice versa.

Classes:
    RecipeViewSet: A viewset that provides the standard actions for the Recipe model.

Functions:
    list: Retrieves a list of all recipes.
    create: Creates a new recipe.
    retrieve: Retrieves a specific recipe by its ID.
    update: Updates an existing recipe.
    partial_update: Partially updates an existing recipe.
    destroy: Deletes a specific recipe by its ID.

Attributes:
    queryset: The base queryset for retrieving recipes.
    serializer_class: The serializer class used for converting Recipe instances.
    permission_classes: The permission classes that define access control for the views.
"""

from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

from core.models import Recipe
from recipe import serializers


class RecipeViewSet(viewsets.ModelViewSet):
    """View for manage recipe APIs."""

    serializer_class = serializers.RecipeDetailSerializer
    queryset = Recipe.objects.all()
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        """Retrieve recipes for authenticated user."""
        return self.queryset.filter(user=self.request.user).order_by("-id")

    def get_serializer_class(self):
        """Return the serializer class for request."""
        if self.action == "list":
            return serializers.RecipeSerializer

        return self.serializer_class
