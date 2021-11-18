from auth_example.models.editorial import Editorial
from rest_framework                import serializers

class EditorialSerializer(serializers.ModelSerializer):
    class Meta:
        model  = Editorial
        fields = ['name_editorial']
