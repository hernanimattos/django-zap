from rest_framework import serializers
from .models import Signer


class SignerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Signer
        fields = '__all__'  #
