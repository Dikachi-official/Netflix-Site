from django.contrib import admin

from netflixapp.models import CustomUser, Movie, Profile, Video
from . import models

# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Profile)
admin.site.register(Movie)
admin.site.register(Video)
