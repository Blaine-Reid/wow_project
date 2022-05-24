from django.http import QueryDict
from django.shortcuts import render

from django.views import View
from food_review.models import Restaurant, TypeOfFood, Tag
from food_review.forms import AddRestaurant
# Create your views here.


class HomePageView(View):
    """Renders home page"""

    def get(self, request):
        return render(request, "index.html")


class SearchView(View):

    def get(self, request):

        try:
            search = request.GET['q']
            restaurants = Restaurant.objects.filter(
                name__startswith=str(search))

            context = {
                "search": search,
                "restaurants":  restaurants
            }

            return render(request, "search.html", context)

        except:

            return render(request, "search.html")
          
          
class AddRestaurantView(View):
    def get(self, request):
        tags=Tag.objects.all()
        return render(request, "add_restaurant.html", {"AddRestaurant": AddRestaurant, "tags": tags})
    def post(self, request):
        restaurant={
        "name":request.POST["resturant_name"],
        "street_address":request.POST["address"],
        "city":request.POST["city"],
        "state":request.POST["state"],
        "zip":request.POST["zip_code"],
        "phone":request.POST["phone_number"],
        "type_food":TypeOfFood(id=int(request.POST["type_food"])),
        "avg_rating": 10 
        }
        new_restaurant=Restaurant.objects.create(**restaurant) 
        new_restaurant.tags.set(request.POST.getlist("tag"))
        print(request.POST)
            
        return render(request, "add_restaurant.html", {"AddRestaurant": AddRestaurant})

        
 
class RestaurantProfile(View):


    def get(self, request, restaurant_id):
        restaurant=Restaurant.objects.get(id=restaurant_id)
        return render(request,"restaurant_profile.html", context={"restaurant_id": restaurant_id, "restaurant": restaurant})
