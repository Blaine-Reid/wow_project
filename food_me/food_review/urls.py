from django.urls import path
from food_review.views import HomePageView, SearchView, RestaurantProfile


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("search/", SearchView.as_view(), name='search'),
    path("restaurant/<int:restaurant_id>",
         RestaurantProfile.as_view(), name='restaurant'),
]
