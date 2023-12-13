from rest_framework import serializers
from .models import Employ
from django.utils import timezone


class EmploySer(serializers.ModelSerializer):
    class Meta:
        model = Employ
        fields = '__all__'

        read_only_fields = ('created_at', 'updated_at')

    def validate_name(self, value):
        if value == "abbas":
            raise serializers.ValidationError("YOU ARE BLOCK")
        else:
            return value

    def validate_age(self, value):
        if value < 18:
            raise serializers.ValidationError("سن شما زیر هیجده سال است")
        else:
            return value

    def create(self, validated_data):
        obj = super().create(validated_data)
        obj.created_at = timezone.now()
        obj.save()
        return obj

    def update(self, instance, validated_data):
        old = instance.created_at

        obj = super().update(instance, validated_data)
        obj.created_at = old
        obj.updated_at = timezone.now()
        obj.save()
        return obj
