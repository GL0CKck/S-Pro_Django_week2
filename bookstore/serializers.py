from rest_framework import serializers

from .models import Store


class CreateStore(serializers.ModelSerializer):

    class Meta:
        model = Store
        fields = ('title', 'description', 'rating')

    def create(self, validated_data):
        return Store.objects.create(**validated_data)