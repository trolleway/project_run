
from rest_framework import serializers
from django.contrib.auth import get_user_model
from .models import Run


class RunSerializer(serializers.ModelSerializer):
    class Meta:
        model = Run
        fields = '__all__'

User = get_user_model()
class UserSerializer(serializers.ModelSerializer):
    type = serializers.SerializerMethodField()
    class Meta:
        model = User

        fields = ['id', 'date_joined', 'username',  'first_name', 'last_name','type']

    def get_type(self, obj):
        if obj.is_staff:
            return 'coach'
        else:
            return 'athlete'
