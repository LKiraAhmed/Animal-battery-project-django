from rest_framework import serializers
from .models import Product,Profile,ShippingAddress,OrderItem,Order,search,DoctorVent,Vent_Photo,Photo,Dogs,AccessoriesDogs,BedsDogs,FoodDogs,FleaTicksDogs,GroomingDogs,PharmacyVitaminsDogs,ToysDogs,TreatsBiscuitsDogs,WetFoodDogs,cats,AccessoriesCats,BedsCats,FoodCats,FleaTicksCats,Groomingcats,Toyscats,TreatsBiscuitsCats,WetFoodCats,fish,AccessoriesFish,FoodFish,Brid,AccessoriesBrid,FoodBrid

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ShippingAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = ShippingAddress
        fields = '__all__'


class OrderItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderItem
        fields = '__all__'

class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'

class Vent_PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vent_Photo
        fields = '__all__'

class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = '__all__'


class DoctorVentSerializer(serializers.ModelSerializer):
    class Meta:
        model = DoctorVent
        fields = '__all__'

class searchSerializer(serializers.ModelSerializer):
    class Meta:
        model = search
        fields = '__all__'

class AccessoriesDogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessoriesDogs
        fields = '__all__'

class BedsDogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BedsDogs
        fields = '__all__'

class FoodDogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodDogs
        fields = '__all__'

class FleaTicksDogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FleaTicksDogs
        fields = '__all__'

class GroomingDogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = GroomingDogs
        fields = '__all__'

class PharmacyVitaminsDogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = PharmacyVitaminsDogs
        fields = '__all__'

class ToysDogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ToysDogs
        fields = '__all__'

class TreatsBiscuitsDogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatsBiscuitsDogs
        fields = '__all__'

class WetFoodDogsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WetFoodDogs
        fields = '__all__'

class AccessoriesCatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessoriesCats
        fields = '__all__'

class BedsCatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = BedsCats
        fields = '__all__'

class FoodCatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodCats
        fields = '__all__'

class FleaTicksCatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = FleaTicksCats
        fields = '__all__'

class GroomingcatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Groomingcats
        fields = '__all__'

class ToyscatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Toyscats
        fields = '__all__'

class TreatsBiscuitsCatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = TreatsBiscuitsCats
        fields = '__all__'

class WetFoodCatsSerializer(serializers.ModelSerializer):
    class Meta:
        model = WetFoodCats
        fields = '__all__'

class AccessoriesFishSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessoriesFish
        fields = '__all__'

class FoodFishSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodFish
        fields = '__all__'

class AccessoriesBridSerializer(serializers.ModelSerializer):
    class Meta:
        model = AccessoriesBrid
        fields = '__all__'

class FoodBridSerializer(serializers.ModelSerializer):
    class Meta:
        model = FoodBrid
        fields = '__all__'

class DogsSerializer(serializers.ModelSerializer):
    accessories_dogs = AccessoriesDogsSerializer(many=True)
    beds_dogs = BedsDogsSerializer(many=True)
    food_dogs = FoodDogsSerializer(many=True)
    flea_ticks_dogs = FleaTicksDogsSerializer(many=True)
    grooming_dogs = GroomingDogsSerializer(many=True)
    pharmacy_vitamins_dogs = PharmacyVitaminsDogsSerializer(many=True)
    toys_dogs = ToysDogsSerializer(many=True)
    treats_biscuits_dogs = TreatsBiscuitsDogsSerializer(many=True)
    wet_food_dogs = WetFoodDogsSerializer(many=True)

    class Meta:
        model = Dogs
        fields = '__all__'

class CatsSerializer(serializers.ModelSerializer):
    accessories_cats = AccessoriesCatsSerializer(many=True)
    beds_cats = BedsCatsSerializer(many=True)
    food_cats = FoodCatsSerializer(many=True)
    flea_ticks_cats = FleaTicksCatsSerializer(many=True)
    grooming_cats = GroomingcatsSerializer(many=True)
    toys_cats = ToyscatsSerializer(many=True)
    treats_biscuits_cats = TreatsBiscuitsCatsSerializer(many=True)
    wet_food_cats = WetFoodCatsSerializer(many=True)

    class Meta:
        model = cats
        fields = '__all__'

class FishSerializer(serializers.ModelSerializer):
    accessories_fish = AccessoriesFishSerializer(many=True)
    food_fish = FoodFishSerializer(many=True)

    class Meta:
        model = fish
        fields = '__all__'

class BridSerializer(serializers.ModelSerializer):
    accessories_brid = AccessoriesBridSerializer(many=True)
    food_brid = FoodBridSerializer(many=True)

    class Meta:
        model = Brid
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    dogs = DogsSerializer()
    cats = CatsSerializer()
    fish = FishSerializer()
    brid = BridSerializer()

    class Meta:
        model = Product
        fields = '__all__'


