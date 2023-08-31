from rest_framework.permissions import  DjangoModelPermissionsOrAnonReadOnly
from rest_framework.viewsets import ModelViewSet

from restaurants.models import Restaurants, FoodItem
from restaurants.serializers import RestaurantSerializer


class RestaurantViewSet(ModelViewSet):
    queryset = Restaurants.objects.all().order_by('-created_on')
    serializer_class =  RestaurantSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

class FoodItemViewSet(ModelViewSet):
    serializer_class =  RestaurantSerializer
    permission_classes = [DjangoModelPermissionsOrAnonReadOnly]

    def get_queryset(self):
        return FoodItem.objects.filter(restaurant_id=self.kwargs['restaurants_pk']).order_by('-created_on')
