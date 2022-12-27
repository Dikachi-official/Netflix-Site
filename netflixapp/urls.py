from django.urls import path
from . import views
from .views import Home, ProfileCreate, ProfileList, MovieList, MovieDetail, PlayMovie


app_name = 'netflixapp'

urlpatterns = [
    path('', Home.as_view(), name='Home'),  #WE USE THIS FORMAT COS OF OUR CLASS BASED VIEW
    path('profiles/', ProfileList.as_view(), name='profilelist'),
    path('profiles/create/', ProfileCreate.as_view(), name='profilecreate'),
    path('watch/<str:profile_id>/', MovieList.as_view(), name='movielist'), #WATCH/THE PROFILE(PROFILE_ID) UUID WHICH IS THE URL
    path('watch/detail/<str:movie_id>/', MovieDetail.as_view(), name='moviedetail'),
    path('watch/play/<str:movie_id>/', PlayMovie.as_view(), name='playmovie'),
]