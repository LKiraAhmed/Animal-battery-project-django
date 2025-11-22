from django.shortcuts import render
from rest_framework import generics

from rest_framework.decorators import api_view 
from rest_framework.response import Response

from django.contrib import auth
from django.contrib.auth.decorators import login_required
from .forms import RegForm
from .decorators import *
from django.contrib.auth.models import User , Group
from django.contrib import messages
from .serializers import ProductSerializer, ProfileSerializer, ShippingAddressSerializer, OrderItemSerializer, \
    OrderSerializer, searchSerializer, DoctorVentSerializer, Vent_PhotoSerializer, PhotoSerializer, \
    DogsSerializer, AccessoriesDogsSerializer, BedsDogsSerializer, FoodDogsSerializer, FleaTicksDogsSerializer, \
    GroomingDogsSerializer, PharmacyVitaminsDogsSerializer, ToysDogsSerializer, TreatsBiscuitsDogsSerializer,\
    WetFoodDogsSerializer, CatsSerializer, AccessoriesCatsSerializer, BedsCatsSerializer, FoodCatsSerializer, \
    FleaTicksCatsSerializer, GroomingcatsSerializer, ToyscatsSerializer, TreatsBiscuitsCatsSerializer, \
    WetFoodCatsSerializer, FishSerializer, AccessoriesFishSerializer, FoodFishSerializer, BridSerializer, \
    AccessoriesBridSerializer,FoodBridSerializer,DogsSerializer
from .models import Profile , Product ,Photo , Order , \
 Product, Profile, ShippingAddress, OrderItem, Order, search, \
    DoctorVent, Vent_Photo, Photo, Dogs, AccessoriesDogs, BedsDogs, FoodDogs, FleaTicksDogs, GroomingDogs,\
    PharmacyVitaminsDogs, ToysDogs, TreatsBiscuitsDogs, WetFoodDogs, cats, AccessoriesCats, BedsCats, \
    FoodCats, FleaTicksCats, Groomingcats, Toyscats, TreatsBiscuitsCats, WetFoodCats, fish, AccessoriesFish,\
    FoodFish, Brid, AccessoriesBrid, FoodBrid
from .utils import cookieCart, cartData, guestOrder
from django.http import JsonResponse
import json
import datetime
from django.views.generic import ListView
from django.db.models import Q
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import ProductSerializer
from django.core import serializers
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


def IS_discount(xxx):
    if xxx == 0 or xxx == '' or xxx == '0':
        return False
    else:
        return True

# Create your views here.
def product_types(request,types):
    products = Product.objects.filter(product_type = types)
    user = request.user
    custom = user.groups.filter(name='customer').exists() 
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    return render(request,'product.html',{'products':products,'customer':custom,'cartItem':cartItems,'types':types})


@login_required(login_url = 'login')
@only_seller
def dashBoard(request):
    user = request.user
    custom = user.groups.filter(name='customer').exists() 
    Product1 = Product.objects.filter(user = user)
    return render(request,'sellerDash.html',{'product':Product1,'customer':custom})


@authandicated
def Doctor_signUP(request):
    form = RegForm()
    phone= request.POST.get('number')
    email= request.POST.get('email')
    vent_phone = request.POST.get('vent_number')
    vent_add = request.POST.get('business-add')
    about = request.POST.get('about')
    profile_pic =request.FILES.get('profile_pic') 
    vent_pic =request.FILES.getlist('vent_pic')
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            prof = form.save()
            user = auth.authenticate(request,username = request.POST.get('username'),password = request.POST.get('password1'))
            doctor_prof = DoctorVent(user = user , email = email , phone = phone , vent_phone= vent_phone 
                                     , address = vent_add , about = about , profile_pic = profile_pic)
            doctor_prof.save()
            group = Group.objects.get(name = 'doctor')
            prof.groups.add(group)
            for img in vent_pic:
                photo = Vent_Photo.objects.create(
                DoctorVent = doctor_prof ,
                vent_img=img,
            )
            if user is not None:
                auth.login(request , user)
                next_url = request.GET.get('next')
                if next_url == '' or next_url == None:
                    next_url = 'home'
                return redirect(next_url)
            else:
                messages.error('please cheak username or pass')
    context = {'form':form}
    return render(request , 'doctor-sign.html',context)




# done
@authandicated
def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        user = User.objects.get(email = email)
        user1 = auth.authenticate(request, username = user.username , password = password)
        if user1 is not None:
            auth.login(request,user1)
            next_url = request.GET.get('next')
            if next_url == '' or next_url == None:
                next_url = 'home'
            return redirect(next_url)
        else:
            messages.error(request, 'please check username or password')
    return render(request,'login.html')
# done
@authandicated
def signup(request):
    form = RegForm()
    phone= request.POST.get('number')
    email= request.POST.get('email')
    
    if request.method == 'POST':
        form = RegForm(request.POST)
        if form.is_valid():
            prof = form.save()
            user = auth.authenticate(request,username = request.POST.get('username'),password = request.POST.get('password1'))
            profileU = Profile(user = user , phone = phone , email = email)
            profileU.save()
            group = Group.objects.get(name = 'customer')
            prof.groups.add(group)
            if user is not None:
                auth.login(request,user)
                next_url = request.GET.get('next')
                if next_url == '' or next_url == None:
                    next_url = 'home'
                return redirect(next_url)
            else:
                messages.error(request, 'please check username or password')
    return render(request,'signup.html',{'form':form})
# done
def logoutUser(request):
    auth.logout(request)
    return redirect('login')
# Done
def home(request):
    discountProduct  =Product.objects.filter(discount = True)
    Dogs = Product.objects.filter(product_type = 'Dog',product_Catecory = 'none')
    Cats = Product.objects.filter(product_type = 'Cat',product_Catecory = 'Food')
    user = request.user
    custom = user.groups.filter(name='customer').exists() 
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    context = {'customer':custom,'discoutProduct':discountProduct, 
               'Dogs':Dogs,'Cats':Cats, 'cartItem':cartItems,'items':items, 'order':order}
    return render(request,'index.html', context)

# done
@login_required(login_url = 'login')
@only_seller
def addProduct(request):
    if request.user:
        user = request.user
        custom = user.groups.filter(name='customer').exists() 
    product_name = request.POST.get('product-name')
    product_sortDes = request.POST.get('sort-des')
    description = request.POST.get('Detail')
    first_file_upload = request.FILES.get('first-file-upload')
    second_file_upload = request.FILES.get('second-file-upload')
    third_file_upload = request.FILES.get('third-file-upload')
    last_file_upload = request.FILES.get('last-file-upload')
    price = request.POST.get('price')
    product_discount_price = request.POST.get('discount-price')
    product_sell_price = request.POST.get('price')
    stock =request.POST.get('stock')
    pet_type = request.POST.get('pet-Type')
    categories = request.POST.get('categories')
    images = [first_file_upload , second_file_upload , third_file_upload , last_file_upload]
    discount = IS_discount(product_discount_price)
    product1 = Product(
        user = user,product_name = product_name,
        product_shot_des = product_sortDes , product_description = description,
        product_price = price, discount = discount ,
        product_discount_price = product_discount_price,
        product_Catecory = categories ,
        product_sell_price = product_sell_price ,
        product_stock= stock,product_type = pet_type,
        slug = product_name
    )
    if request.method == 'POST'and request.FILES:
        product1.save()
        prodct11 = Product.objects.get(product_name = product_name)
        prodct11.product_img = first_file_upload
        prodct11.save()
        for x in images:
            pic = Photo.objects.create(
                product= prodct11,
                product_img = x
            )
        return redirect('DashBoard')
    return render(request,'add-product.html',{'customer':custom})
# done
@login_required(login_url = 'login')
def seller(request):
    business_name = request.POST.get('business-name')
    business_add = request.POST.get('business-add')
    about = request.POST.get('about')
    business_phone = request.POST.get('phone')
    user = request.user
    profile_user = Profile.objects.get(user = user)
    profile_user.business_name = business_name
    profile_user.address = business_add
    profile_user.about = about
    profile_user.business_phone = business_phone
    user = request.user
    custom = user.groups.filter(name='customer').exists() 
    if request.method == 'POST':
        group = Group.objects.get(name = 'seller')
        groupCus = Group.objects.get(name = 'customer')
        user.groups.add(group)
        user.groups.remove(groupCus)
        profile_user.save()
        return redirect('DashBoard')
    return render(request,'seller.html',{'customer':custom})
# done
def product(request):
    products = Product.objects.all()
    user = request.user
    custom = user.groups.filter(name='customer').exists() 
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    return render(request,'product.html',{'products':products,'customer':custom , 'cartItem':cartItems})
# Done
def home(request):
    user = request.user
    custom = user.groups.filter(name='customer').exists() 
    product1  =Product.objects.filter(discount = True)
    product2 = Product.objects.filter(product_type = 'Dog')
    product3 = Product.objects.filter(product_type = 'Cat')
    context = {'customer':custom,'discoutProduct':product1, 
               'Dogs':product2,'Cats':product3}
    return render(request,'index.html', context)
# Done
def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    print('Action:', action)
    print('Product:', productId)

    customer = request.user
    customer = Profile.objects.get(user = customer)
    product = Product.objects.get(id=productId)
    order, created = Order.objects.get_or_create(customer=customer, complete=False)

    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    if action == 'add':
        orderItem.quantity = (orderItem.quantity + 1)
    elif action == 'remove':
        orderItem.quantity = (orderItem.quantity - 1)

    orderItem.save()

    if orderItem.quantity <= 0:
        orderItem.delete()

    return JsonResponse('Item was added', safe=False)
# Done
def processOrder(request):
    transaction_id = datetime.datetime.now().timestamp()
    data = json.loads(request.body)

    if request.user.is_authenticated:
        customer = request.user
        customer = Profile.objects.get(user = customer)
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
    else:
        customer, order = guestOrder(request, data)

    total = float(data['form']['total'])
    order.transaction_id = transaction_id

    if total == order.get_cart_total:
        order.complete = True
    order.save()

    if order.shipping == True:
        ShippingAddress.objects.create(
        customer=customer,
        order=order,
        address=data['shipping']['address'],
        city=data['shipping']['city'],
        state=data['shipping']['state'],
        zipcode=data['shipping']['zipcode'],
        )

    return JsonResponse('Payment submitted..', safe=False)
# Done-test
def productDetail(request):
    user = request.user
    custom = user.groups.filter(name='customer').exists() 
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    return render(request,'product-detail.html',{'customer':custom, 'cartItem':cartItems})
# Done
def productDetailList(request,slug):
    product_data = Product.objects.get(slug = slug)
    prodctImgs = Photo.objects.filter(product = product_data)
    user = request.user
    custom = user.groups.filter(name='customer').exists() 
    product1  =Product.objects.filter(discount = True)
    product2 = Product.objects.filter(product_type = 'Dog',product_Catecory = 'none')
    data = cartData(request)
    cartItems = data['cartItems']
    order = data['order']
    items = data['items']
    return render(request,'product-detail.html',{'data':product_data, 'customer':custom,
                                                 'discoutProduct':product1, 'Dogs':product2
                                                 ,'imgs':prodctImgs , 'cartItem':cartItems})
# Done
def card(request):
    user = request.user
    custom = user.groups.filter(name='customer').exists() 
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems ,'customer':custom}
    return render(request,'card.html',context)
# Done
@login_required(login_url = 'login')
def checkout(request):
    user = request.user
    custom = user.groups.filter(name='customer').exists() 
    data = cartData(request)

    cartItems = data['cartItems']
    order = data['order']
    items = data['items']

    context = {'items':items, 'order':order, 'cartItems':cartItems , 'customer':custom }
    return render(request,'checkout.html',context)

def search_products(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            
            products = Product.objects.filter(product_name__icontains=query)


            return render(request, 'product_list.html', {
                'products': products
            })
        else:
            return JsonResponse({
                'message':'failed to load',
                'status':500
            }, safe=False)


@api_view(['GET'])
def search_api(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            products = Product.objects.filter(product_name__icontains=query)

          
            return JsonResponse({
                'data': json.loads(serializers.serialize('json',products)),
                'message':'successfully',
                'status':200
            },safe=True)
        else:
            return Response({
                'message':'failed to load data',
                'status':500
            })




def product_detail(request, slug):
    product = Product.objects.get(slug=slug)
    photos = Vent_Photo.objects.filter(product=product)
    context = {'product': product, 'photos': photos}
    return render(request, 'product_detail.html', context)


@csrf_exempt
def product_search(request):
    if request.method == 'GET':
        query = request.GET.get('q')
        if query:
            products = Product.objects.filter(name__icontains=query)
            data = serializers.serialize('json', products)
            return JsonResponse(data, safe=False)
        else:
            return JsonResponse([], safe=False)
        


        
class ProductList(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProfileList(generics.ListCreateAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

class ShippingAddressList(generics.ListCreateAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer

class ShippingAddressDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ShippingAddress.objects.all()
    serializer_class = ShippingAddressSerializer

class OrderItemList(generics.ListCreateAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = OrderItem.objects.all()
    serializer_class = OrderItemSerializer

class OrderList(generics.ListCreateAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class OrderDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer

class Vent_PhotoList(generics.ListCreateAPIView):
    queryset = Vent_Photo.objects.all()
    serializer_class = Vent_PhotoSerializer

class Vent_PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Vent_Photo.objects.all()
    serializer_class = Vent_PhotoSerializer

class PhotoList(generics.ListCreateAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class PhotoDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer

class DoctorVentList(generics.ListCreateAPIView):
    queryset = DoctorVent.objects.all()
    serializer_class = DoctorVentSerializer

class DoctorVentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = DoctorVent.objects.all()
    serializer_class = DoctorVentSerializer

class searchList(generics.ListCreateAPIView):
    queryset = search.objects.all()
    serializer_class = searchSerializer

class searchDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = search.objects.all()
    serializer_class = searchSerializer

class AccessoriesDogsList(generics.ListCreateAPIView):
    queryset = AccessoriesDogs.objects.all()
    serializer_class = AccessoriesDogsSerializer

class AccessoriesDogsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AccessoriesDogs.objects.all()
    serializer_class = AccessoriesDogsSerializer

class BedsDogsList(generics.ListCreateAPIView):
    queryset = BedsDogs.objects.all()
    serializer_class = DogsSerializer

class BedsDogsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BedsDogs.objects.all()
    serializer_class = BedsDogsSerializer

class FoodDogsList(generics.ListCreateAPIView):
    queryset = FoodDogs.objects.all()
    serializer_class = FoodDogsSerializer

class FoodDogsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodDogs.objects.all()
    serializer_class = FoodDogsSerializer

class FleaTicksDogsList(generics.ListCreateAPIView):
    queryset = FleaTicksDogs.objects.all()
    serializer_class = FleaTicksDogsSerializer

class FleaTicksDogsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FleaTicksDogs.objects.all()
    serializer_class = FleaTicksDogsSerializer

class GroomingDogsList(generics.ListCreateAPIView):
    queryset = GroomingDogs.objects.all()
    serializer_class = GroomingDogsSerializer

class GroomingDogsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = GroomingDogs.objects.all()
    serializer_class = GroomingDogsSerializer

class PharmacyVitaminsDogsList(generics.ListCreateAPIView):
    queryset = PharmacyVitaminsDogs.objects.all()
    serializer_class = PharmacyVitaminsDogsSerializer

class PharmacyVitaminsDogsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = PharmacyVitaminsDogs.objects.all()
    serializer_class = PharmacyVitaminsDogsSerializer

class ToysDogsList(generics.ListCreateAPIView):
    queryset = ToysDogs.objects.all()
    serializer_class = ToysDogsSerializer

class ToysDogsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = ToysDogs.objects.all()
    serializer_class = ToysDogsSerializer

class TreatsBiscuitsDogsList(generics.ListCreateAPIView):
    queryset = TreatsBiscuitsDogs.objects.all()
    serializer_class = TreatsBiscuitsDogsSerializer

class TreatsBiscuitsDogsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TreatsBiscuitsDogs.objects.all()
    serializer_class = TreatsBiscuitsDogsSerializer

class WetFoodDogsList(generics.ListCreateAPIView):
    queryset = WetFoodDogs.objects.all()
    serializer_class = WetFoodDogsSerializer

class WetFoodDogsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WetFoodDogs.objects.all()
    serializer_class = WetFoodDogsSerializer

class AccessoriesCatsList(generics.ListCreateAPIView):
    queryset = AccessoriesCats.objects.all()
    serializer_class = AccessoriesCatsSerializer

class AccessoriesCatsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AccessoriesCats.objects.all()
    serializer_class = AccessoriesCatsSerializer

class BedsCatsList(generics.ListCreateAPIView):
    queryset = BedsCats.objects.all()
    serializer_class = BedsCatsSerializer

class BedsCatsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = BedsCats.objects.all()
    serializer_class = BedsCatsSerializer

class FoodCatsList(generics.ListCreateAPIView):
    queryset = FoodCats.objects.all()
    serializer_class = FoodCatsSerializer

class FoodCatsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodCats.objects.all()
    serializer_class = FoodCatsSerializer

class FleaTicksCatsList(generics.ListCreateAPIView):
    queryset = FleaTicksCats.objects.all()
    serializer_class = FleaTicksCatsSerializer

class FleaTicksCatsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FleaTicksCats.objects.all()
    serializer_class = FleaTicksCatsSerializer

class GroomingcatsList(generics.ListCreateAPIView):
    queryset = Groomingcats.objects.all()
    serializer_class = GroomingcatsSerializer

class GroomingcatsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Groomingcats.objects.all()
    serializer_class = GroomingcatsSerializer

class ToyscatsList(generics.ListCreateAPIView):
    queryset = Toyscats.objects.all()
    serializer_class = ToyscatsSerializer

class ToyscatsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Toyscats.objects.all()
    serializer_class = ToyscatsSerializer

class TreatsBiscuitsCatsList(generics.ListCreateAPIView):
    queryset = TreatsBiscuitsCats.objects.all()
    serializer_class = TreatsBiscuitsCatsSerializer

class TreatsBiscuitsCatsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TreatsBiscuitsCats.objects.all()
    serializer_class = TreatsBiscuitsCatsSerializer

class WetFoodCatsSerializer(generics.RetrieveDestroyAPIView) :
   queryset = WetFoodCats.objects.all()
   serializer_class = WetFoodCatsSerializer

class WetFoodCatsDetail(generics.RetrieveUpdateAPIView) :
   queryset = WetFoodCats.objects.all()
   serializer_class = WetFoodCatsSerializer

class CatsSerializer(generics.RetrieveUpdateAPIView):
    queryset=cats.objects.all()
    serializer_class=CatsSerializer

class FishSerializer(generics.RetrieveUpdateAPIView):
    queryset=fish.objects.all()
    serializer_class=FishSerializer

class AccessoriesFishList(generics.ListCreateAPIView):
    queryset = AccessoriesFish.objects.all()
    serializer_class = AccessoriesFishSerializer

class AccessoriesFishDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AccessoriesFish.objects.all()
    serializer_class = AccessoriesFishSerializer

class FoodFishList(generics.ListCreateAPIView):
    queryset = FoodFish.objects.all()
    serializer_class = FoodFishSerializer

class FoodFishDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodFish.objects.all()
    serializer_class = FoodFishSerializer

class BridList(generics.ListCreateAPIView):
    queryset = Brid.objects.all()
    serializer_class = BridSerializer

class BridDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brid.objects.all()
    serializer_class = BridSerializer

class AccessoriesBridList(generics.ListCreateAPIView):
    queryset = AccessoriesBrid.objects.all()
    serializer_class = AccessoriesBridSerializer

class AccessoriesBridDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = AccessoriesBrid.objects.all()
    serializer_class = AccessoriesBridSerializer

class FoodBridlist(generics.ListCreateAPIView):
    queryset = FoodBrid.objects.all()
    serializer_class = FoodBridSerializer
        
class FoodBridDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = FoodBrid.objects.all()
    serializer_class = FoodBridSerializer

class Dogslist(generics.ListCreateAPIView):
    queryset = Dogs.objects.all()
    serializer_class = DogsSerializer

class DogsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Dogs.objects.all()
    serializer_class = DogsSerializer
            
