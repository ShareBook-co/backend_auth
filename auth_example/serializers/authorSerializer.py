from auth_example.models.author import Author
from rest_framework             import serializers

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Author
        fields = ['name_author']