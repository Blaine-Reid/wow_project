from django.http import QueryDict
from django.shortcuts import render

from django.views import View
from food_review.models import Restaurant

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


class RestaurantProfile(View):

    def get(self, request, restaurant_id):
        return render(request,"restaurant_profile.html")