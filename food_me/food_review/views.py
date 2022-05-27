from xml.etree.ElementTree import Comment
from django.http import QueryDict
from django.shortcuts import render, redirect
from datetime import datetime
from django.views import View
from food_review.models import Restaurant, TypeOfFood, Tag, Comment
from food_review.forms import AddRestaurant, AddRestaurantTags
# Create your views here.


def RenderRestaurant(request, restaurant_id):
    restaurant = Restaurant.objects.get(id=restaurant_id)
    tags = restaurant.tags.all()
    comments = Comment.objects.all().filter(restaurant_id=restaurant_id)

    return render(
        request,
        "restaurant_profile.html",
        context={
            "restaurant_id": restaurant_id,
            "restaurant": restaurant,
            "tags": tags,
            "comments": comments
        })


class HomePageView(View):
    """Renders home page"""

    def get(self, request):
        return render(request, "index.html")


class SearchView(View):
    '''Search for a restaurant'''

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
    '''Add a restaurant'''

    def get(self, request):
        tags = Tag.objects.all()
        return render(request, "add_restaurant.html", {"AddRestaurant": AddRestaurant, "tags": tags,  "AddRestaurantTags": AddRestaurantTags})

    def post(self, request):
        restaurant = {
            "name": request.POST["resturant_name"],
            "street_address": request.POST["address"],
            "city": request.POST["city"],
            "state": request.POST["state"],
            "zip": request.POST["zip_code"],
            "phone": request.POST["phone_number"],
            "type_food": TypeOfFood(id=int(request.POST["type_food"])),
            "avg_rating": 10
        }
        new_restaurant = Restaurant.objects.create(**restaurant)
        new_restaurant.tags.set(request.POST.getlist("tag"))

        return render(request, "add_restaurant.html", {"AddRestaurant": AddRestaurant, "AddRestaurantTags": AddRestaurantTags})


class RestaurantProfile(View):
    '''View comments and details of restaurant'''

    def get(self, request, restaurant_id):
        return RenderRestaurant(request, restaurant_id)

    def post(self, request, restaurant_id):
        comment = {
            'body': request.POST['review'],
            'rating': request.POST['rating'],
            'date_created': datetime.today(),
            'date_updated': datetime.today(),
            'restaurant_id': restaurant_id
        }
        Comment.objects.create(**comment)
        return RenderRestaurant(request, restaurant_id)


class Comments(View):
    '''Modifying comments of a restaurant'''

    def post(self, request, restaurant_id, comment_id):

        comment = Comment.objects.get(id=comment_id)

        # # UPDATE COMMENT
        if 'patch' in request.POST:
            comment.body = request.POST['content']
            comment.date_updated = datetime.today()
            comment.rating = request.POST['rating']
            comment.save()

        # DELETE A COMMENT
        if 'delete' in request.POST:
            comment.delete()
            return redirect(f'/restaurant/{restaurant_id}')

        return RenderRestaurant(request, restaurant_id)
