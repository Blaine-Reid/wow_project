from django.db import models
from phonenumber_field.modelfields import PhoneNumberField


# ------------------------------------------------------------
# -------------------- TYPE OF FOOD --------------------------
# ------------------------------------------------------------
class TypeOfFood(models.Model):
    """Type of food served by restaurant"""

    # Type of food
    type_of_food = models.CharField(
        help_text="Type of food served by restaurant"
    )

# ------------------------------------------------------------
# ----------------- RESTAURANT MODEL  ------------------------
# ------------------------------------------------------------
# Create your models here.
class Restaurant(models.Model):
    """A restaurant and its details"""

    # Name of the Restaurant
    name = models.CharField(
        help_text="Name of the restaurant.",
        max_length=250,
        required= True
            
    )
    #Street address 
    street_address = models.CharField(
        help_text="Address of the restaurant.",
        max_length=250,
        required= True
    )
    # City
    city = models.CharField(
        help_text="City restaurant is located in.",
        max_length=100,
        required= True
    )
    # Zip code (5-digit)
    zip = models.IntegerField(
        help_text="Zip code of restaurant location.",
        max_length=5,
        required= True
    )
    # Phone (###)###-####
    phone = PhoneNumberField(
        null=False,
        blank=False, 
        unique=True,
        required= True
        )

    # Aggregated rating from all ratings given
    avg_rating = models.FloatField(
        help_text="Average rating of all ratings given.",
        max_length=2
    )

    # Type of food restaurant serves
    type_food = models.ForeignKey(
        TypeOfFood,
        on_delete=models.CASCADE
    )
