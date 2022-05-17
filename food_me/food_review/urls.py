from django.urls import path
from food_review.views import HomePageView, SearchView


urlpatterns = [
    path("", HomePageView.as_view(), name="home"),
    path("search/", SearchView.as_view(), name='search'),
    # path("restaurant/", RestaurantView.as_view(), name='restaurant'),

]
