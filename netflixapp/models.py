from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid
from datetime import datetime

# Create your models here.

CATEGORIES = (
    ('General','General'),      #others and kids category
    ('Kids', 'Kids'),
)

MOVIE_SELECTION =(
    ('seasonal', 'Seasonal'),
    ('single', 'Single'),
)



class CustomUser(AbstractUser):    #To make a user our own way 
    profiles = models.ManyToManyField('Profile', blank=True)  #for one to have access to many profiles(e.g parents for kids.(PG))


class Profile(models.Model): #AND NOW FOR THAT PROFILE ABOVE
    name = models.CharField(max_length = 200)
    age_limit = models.CharField(choices=CATEGORIES, max_length= 15)  #TOMAKE MANDATORY FOR USER TO CHOOSE AGE CATEGORY
    uuid = models.UUIDField(default=uuid.uuid4)   #TO KEEP TRACK OF INDIVIDUALS PROFILE WITH A UNIQUE ID

    def __str__(self):      #DUNDER METHOD TO RETURN NAME OF OUR PROFILE NAME IN THE DATABASE
        return self.name


class Movie(models.Model):
    title = models.CharField(max_length = 200)
    description = models.TextField(blank=True, null=True)  #MIGHT NOT HAVE DESCRIPTION SO IN SUCH S CASE IT SEES BLANK
    created = models.DateTimeField(auto_now_add=True)      #CREATED TIME OF THE MOVIE
    uuid = models.UUIDField(default=uuid.uuid4)   #KEEP TRACK OF MOVIE WITH AUNIQUE ID
    genre = models.CharField(choices=MOVIE_SELECTION, max_length= 15)   #LIKE THE TYPE EITHER SEASONAL OR SINGLE
    video = models.ManyToManyField('Video')    #A MOVIE MIGHT BE SINGLE WITH MANY EPISODES SO MANY2MANY IS REQUIRED
    image = models.ImageField(upload_to ='covers')
    age_limit = models.CharField(choices=CATEGORIES, max_length = 10)

    def __str__(self):      #DUNDER METHOD TO RETURN NAME OF OUR TITLE IN THE DATABASE
        return self.title


class Video(models.Model):
    title = models.CharField(max_length = 200)
    file = models.FileField(upload_to='movies')

    def __str__(self):      #DUNDER METHOD TO RETURN TITLE OF VIDEO IN THE DATABASE
        return self.title



