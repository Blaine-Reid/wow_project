from django.urls import path
from food_review.views import HomePageView

urlpatterns = [
    path("", HomePageView.as_view(), name="home") 
]