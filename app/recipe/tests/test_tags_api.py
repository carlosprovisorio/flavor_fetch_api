"""
Tests for the tags API.

This module contains unit tests for the tags API endpoints. It ensures that
the API behaves as expected when creating, retrieving, updating, and deleting
tags.

"""

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient

from core.models import Tag

from recipe.serializers import TagSerializer

TAGS_URL = reverse("recipe:tag-list")


def create_user(email="user@example.com", password="testpass123"):
    """Create and return a user."""
    return get_user_model().objects.create_user(email=email, password=password)
