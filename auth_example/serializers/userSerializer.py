from rest_framework           import serializers
from auth_example.models.user import User

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'name',
                  'email', 'address', 'phone', 'gender']

    def create(self, validated_data):
        userInstance = User.objects.create(**validated_data)
        return userInstance

    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)

        return {
            'id':       user.id,
            'username': user.username,
            'name':     user.name,
            'email':    user.email,
            'address':  user.address,
            'phone':    user.phone,
            'gender':   user.gender,
        }
