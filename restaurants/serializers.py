from rest_framework import serializers

from restaurants.models import Restaurants


class FoodItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = ('id', 'name','created_on', 'updates_on')
        read_only_field = ('id',)
class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurants
        fields = ('id', 'name', 'address', 'phone_number', 'created_on', 'updates_on')
        read_only_field = ('id',)


