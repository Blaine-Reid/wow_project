from django.shortcuts import render

from django.views import View
from food_review.models import Restaurant

# Create your views here.

class HomePageView(View):
    def get(self, request):
        return render(request, "home.html")