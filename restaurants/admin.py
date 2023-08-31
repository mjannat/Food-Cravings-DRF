from django.contrib import admin

from restaurants.models import Restaurants, FoodItem

class FoodItemsInline(admin.TabularInline):
    model =FoodItem
    extra = 1

@admin.register(Restaurants)
class RestaurantsAdmin(admin.ModelAdmin):
    list_display = ['name','address']

@admin.register(FoodItem)
class RestaurantsAdmin(admin.ModelAdmin):
    list_display = ['name']

