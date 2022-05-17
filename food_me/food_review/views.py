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

            restaurants = Restaurant.objects.filter(name__contains=str(search))

            context = {
                "search": search,
                "restaurants":  restaurants
            }
            print(restaurants)
            return render(request, "search.html", context=context)

        except:
            # context = {
            #     "search": ''
            # }

            return render(request, "search.html", context=context)
