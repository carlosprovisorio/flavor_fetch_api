"""
URL mappings for the recipe app.

This module defines the URL patterns for the recipe application, mapping
various URL paths to their corresponding views. It includes routes for
listing recipes, viewing individual recipe details, creating new recipes,
updating existing recipes, and deleting recipes.

Routes:
- /recipes/ : Lists all recipes.
- /recipes/<int:id>/ : Displays details of a specific recipe identified by its ID.
- /recipes/new/ : Provides a form to create a new recipe.
- /recipes/<int:id>/edit/ : Provides a form to edit an existing recipe identified by its ID.
- /recipes/<int:id>/delete/ : Deletes a specific recipe identified by its ID.

Each route is associated with a view function that handles the request and
returns an appropriate response.
"""

from django.urls import (
    path,
    include,
)

from rest_framework.routers import DefaultRouter

from recipe import views

router = DefaultRouter()
router.register("recipes", views.RecipeViewSet)
router.register("tags", views.TagViewSet)
app_name = "recipe"

urlpatterns = [
    path("", include(router.urls)),
]
