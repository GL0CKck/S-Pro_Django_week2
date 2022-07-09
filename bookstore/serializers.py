from rest_framework import serializers

from .models import Store


class CreateStoreSerializer(serializers.ModelSerializer):
    rating = serializers.CharField()

    class Meta:
        model = Store
        fields = ('title', 'description', 'rating')

    def validate(self, data):
        rating = data.get('rating')
        if int(rating) > 100:
            raise serializers.ValidationError('Rating cannot be more than 100')
        else:
            return {
                'rating': rating
            }

    def create(self, validated_data):
        return Store.objects.create(**validated_data)