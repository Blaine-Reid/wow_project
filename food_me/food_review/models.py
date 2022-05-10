from xml.etree.ElementTree import Comment
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.core.validators import MaxValueValidator, MinValueValidator 

# ------------------------------------------------------------
# -------------------- TYPE OF FOOD --------------------------
# ------------------------------------------------------------
class TypeOfFood(models.Model):
    """Type of food served by restaurant"""

    # Type of food
    type_of_food = models.CharField(
        max_length= 50,
        help_text="Type of food served by restaurant"
    )

    # Return a string
    def __str__(self) -> str:
        return self.type_of_food

# ------------------------------------------------------------
# ----------------------- TAGS -------------------------------
# ------------------------------------------------------------

class Tag(models.Model):
    """Tags that classify a restaurant"""

    # Descriptive tag 
    tag_name = models.CharField(
        max_length= 25,
        help_text="Descriptive tag"
    )

    # Return a string
    def __str__(self) -> str:
        return self.tag_name

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
            
    )
    #Street address 
    street_address = models.CharField(
        help_text="Address of the restaurant.",
        max_length=250,
    )
    # City
    city = models.CharField(
        help_text="City restaurant is located in.",
        max_length=100,
        # required= True
    )
    # State
    state = models.CharField(
        help_text="State of restaurant location.",
        max_length=2
    )
    # Zip code (5-digit)
    zip = models.CharField(
        help_text="Zip code of restaurant location.",
        max_length=5
    )
    # Phone (###)###-####
    phone = PhoneNumberField(
        null=False,
        blank=False, 
        unique=True,
        )
    # Aggregated rating from all ratings given
    avg_rating = models.FloatField(
        help_text="Average rating of all ratings given.",
        max_length=2
    )
    # Type of food restaurant serves
    type_food = models.ForeignKey(
        TypeOfFood,
        help_text="Type of food served by restaurant.",
        on_delete=models.CASCADE
    )

    # Tags describing the restaurant
    tags = models.ManyToManyField(Tag)

    # Return a string
    def __str__(self) -> str:
        return self.name

# ------------------------------------------------------------
# ----------------------- COMMENT ----------------------------
# ------------------------------------------------------------

class Comment(models.Model):
    """Comment about a experience at Restaurant"""

    # Body of the comment
    body = models.TextField(
        help_text="The comment text"
    )
    # 1 to 10 rating 
    rating = models.PositiveIntegerField(
        help_text="The rating the reviewer has given.",
        validators=[MinValueValidator(1),MaxValueValidator(10)]
    )
    # Date comment was created
    date_created = models.DateTimeField(
        auto_now_add=True,
        help_text= "The date and time the review was created."
    )
    # Date comment was updated
    date_updated = models.DateTimeField(
        null=True,
        help_text="The date and time the review was last edited"
    )
    # Restaurant comment is created for
    restaurant = models.ForeignKey(
        Restaurant,
        on_delete=models.CASCADE,
        help_text="The Restaurant that the review is for."
    )

    # Return a string
    def __str__(self) -> str:
        return self.body




