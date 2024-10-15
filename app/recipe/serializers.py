"""
Serializers for recipe APIs.

This module contains serializers used to convert complex data types, such as
querysets and model instances, into native Python datatypes that can then be
easily rendered into JSON, XML, or other content types. These serializers also
provide deserialization, allowing parsed data to be converted back into complex
types, after first validating the incoming data.

Classes:
    RecipeSerializer: A serializer for the Recipe model, handling the conversion
                      of Recipe instances to and from JSON.
    IngredientSerializer: A serializer for the Ingredient model, managing the
                          conversion of Ingredient instances to and from JSON.
    StepSerializer: A serializer for the Step model, facilitating the conversion
                    of Step instances to and from JSON.

Each serializer class includes fields that correspond to the model fields, and
may include custom validation and transformation logic to ensure data integrity
and proper formatting.
"""

from rest_framework import serializers

from core.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for recipes."""

    class Meta:
        model = Recipe
        fields = [
            "id",
            "title",
            "time_minutes",
            "price",
            "link",
        ]
        read_only_fields = ["id"]
