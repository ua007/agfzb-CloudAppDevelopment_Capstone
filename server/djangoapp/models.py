from django.db import models
from django.utils.timezone import now
from django.core import serializers 
import uuid
import json

# Create your models here.

# <HINT> Create a Car Make model `class CarMake(models.Model)`:
# - Name
# - Description
# - Any other fields you would like to include in car make model
# - __str__ method to print a car make object
class CarMake(models.Model):
    name = models.CharField(null=False, max_length=20, default='undefined')
    description = models.TextField(null=True)
    def __str__(self):
        return self.name + ": " + self.description

# <HINT> Create a Car Model model `class CarModel(models.Model):`:
# - Many-To-One relationship to Car Make model (One Car Make has many Car Models, using ForeignKey field)
# - Name
# - Dealer id, used to refer a dealer created in cloudant database
# - Type (CharField with a choices argument to provide limited choices such as Sedan, SUV, WAGON, etc.)
# - Year (DateField)
# - Any other fields you would like to include in car model
# - __str__ method to print a car make object
class CarModel(models.Model):
    make = models.ForeignKey(CarMake, null=False, on_delete=models.CASCADE)  
    name = models.CharField(null=False, max_length=40, default='undefined')
    id = models.IntegerField(default=1,primary_key=True)        

    # One way -------------------
    # car_type = models.CharField(max_length=20, choices=[('Sedan', 'sedan'), ('SUV', 'suv'), ('WAGON', 'wagon')])

    # Another way -------------------
    type = models.CharField(
        null=False,
        max_length=20,
        choices=[('Sedan', 'sedan'), ('SUV', 'suv'), ('WAGON', 'wagon')],
        default='Sedan'
    )
    
    year = models.DateTimeField('date designed')
    def __str__(self):
        return self.type

# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:
    def __init__(self, address, city, full_name, id, lat, long, st, zip):
        self.address = address
        self.city = city
        self.full_name=full_name
        self.id = id
        self.lat = lat
        self.long = long
        self.st = st
        self.zip = zip
    def __str__(self):
        return "Dealer name: " + self.full_name

# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
    def __init__(self, dealership, name, purchase, review):
        # Required attributes
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        # Optional attributes
        self.purchase_date = ""
        self.purchase_make = ""
        self.purchase_model = ""
        self.purchase_year = ""
        self.sentiment = ""
        self.id = ""
    def __str__(self):
        return "Review: " + self.review
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                            sort_keys=True, indent=4)

class ReviewPost:
    def __init__(self, dealership, name, purchase, review):
        # Required attributes
        self.dealership = dealership
        self.name = name
        self.purchase = purchase
        self.review = review
        # Optional attributes
        self.purchase_date = ""
        self.car_make = ""
        self.car_model = ""
        self.car_year = ""
    def to_json(self):
        return json.dumps(self, default=lambda o: o.__dict__,
                            sort_keys=True, indent=4)
