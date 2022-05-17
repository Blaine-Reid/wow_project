from django.shortcuts import render

from django.views import View
from food_review.models import Restaurant
from food_review.forms import AddRestaurant
# Create your views here.

class HomePageView(View):
    """Renders home page"""
    def get(self, request):
        return render(request, "index.html")

class SearchView(View):
    """Renders and processes searches"""
    def get(self, request, query):
        print(QueryDict.items())
        return render(request, "search.html", {'query': query})

class ReviewView(View):
    def get(self, request):
        return render(request)

class AddRestaurantView(View):
    def get(self, request):
        return render(request, "add_restaurant.html", {"AddRestaurant": AddRestaurant})

class RestaurantProfileView(View):
    def get(self, request):
        return render(request)
        
        
