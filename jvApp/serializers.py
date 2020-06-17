from rest_framework import serializers
from jvApp.models import User, WildCard

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'passhash', 'email', 'timer_countdown', 'timer_enabled')

class WildCardSerializer(serializers.ModelSerializer):
    class Meta:
        model = WildCard
        fields = ('id', 'name', 'description', 'default_ac', 'default_max_hp', 'user_fk')
