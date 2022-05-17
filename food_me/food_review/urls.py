from django.urls import path
from food_review.views import HomePageView, SearchView, AddRestaurantView
 

urlpatterns = [
    path("", HomePageView.as_view(), name="home"), 
    # path("search?query=<query>", SearchView.as_view(), name="search"),
    path("search/<query>", SearchView.as_view(), name="search"),
    path("add/", AddRestaurantView.as_view(), name="add_restaurant" )
]