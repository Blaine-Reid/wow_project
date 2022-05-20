from food_review.models import TypeOfFood, Tag
from django import forms



class AddRestaurant(forms.Form):
    """Add a restaurant"""
    
    resturant_name = forms.CharField(label = "Restaurant Name", max_length = 255)
    address = forms.CharField(label = "Street Address", max_length = 255)
    city = forms.CharField(label = "City", max_length=100)
    state = forms.CharField(label = "State", max_length=50)
    zip_code = forms.CharField(label = "Zip Code", max_length=5)
    phone_number = forms.CharField(label = "Phone Number", max_length = 10)
    type_food = forms.MultipleChoiceField( choices=[(tq.pk, tq.__str__()) for tq in TypeOfFood.objects.all()])
    tag = forms.MultipleChoiceField(choices = [(tq.pk, tq.__str__()) for tq in Tag.objects.all()])



class AddRestaurantReview(forms.Form):
    rating = forms.IntegerField(label = "How would you rate this restaurant?", max_value = 5)
    review = forms.CharField(label = "Your review", max_length = 500)