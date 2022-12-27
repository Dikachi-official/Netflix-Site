from django.shortcuts import render, redirect
from django.views import View  #To be able to use class based views
from django.contrib.auth.decorators import login_required  # FOR LOGIN AUTHENTICATION
from django.utils.decorators import method_decorator
import netflixapp    #FOR LOGIN AUTHENTICATION
from netflixapp.forms import ProfileForm
from netflixapp.models import Movie, Profile   



# Create your views here.     (1)
class Home(View): # a class to inherit from the view imported 
    def get(self, request, *args, **kwargs):
        if request.user.is_authenticated:       #ONCE USER IS LOGGED IN
            return redirect('netflixapp:profilelist')   #REDIRECT TO THE USER TO URL WITH THIS PATH NAME(profiles/)
        return render(request,'index.html')     #ELSE RENDER INDEX TEMPLATE



# TO CREATE A PROFILE LIST(CHILD PROFILE)     (2)
method_decorator(login_required, name='dispatch')      #FOR THE SAKE OF USING THE AUTH FUNCTIONALITY IMPORTED
class ProfileList(View):        # a class to inherit from the view imported
    def get(self, request, *args, **kwargs):
        profiles = request.user.profiles.all()   # TO GET ALL OBJECT INFO FROM OUR CUSTOM-USER IN MODELS(CHILD PROFILE) 
        context = {
            'profiles':profiles
        }
        return render(request, 'profilelist.html', context) 



# TO CREATE A PROFILE (PARENT PROFILE)       (3)
method_decorator(login_required, name='dispatch')    
class ProfileCreate(View):     # a class to inherit from the view imported

    #GET REQUEST
    def get(self, request, *args, **kwargs):    #IF THE FORM IS GET REQUEST(FORM IS EITHER GET OR POST REQUEST)

        form = ProfileForm()   #FROM OUR FORMS.PY
        context = {
            'form':form
        }
        return render(request, 'createprofile.html', context) 

    #POST REQUEST
    def post(self, request, *args, **kwargs):    #IF THE FORM IS POST REQUEST(FORM IS EITHER GET OR POST REQUEST)

        form = ProfileForm(request.POST or None)   #FROM OUR FORMS.PY, we collect the request method, if it an input exists or not
        if form.is_valid():  #IF THE USER CREATED A PROFILE OR GIVES A VALID RESPONSE
            profile = Profile.objects.create(**form.cleaned_data)  #collect the valid response data and pass to our model db
            if profile:  #IF THERES A PARENT PROFILE 
                request.user.profiles.add(profile)   #ADD CHILD PROFILE TO THE EXISTING PARENT PROFILE
                return redirect('netflixapp:profilelist')  #TO PROFILELIST WHERE ALL PROFILES ARE LOCATED
        context = {             #ELSE IF NO VALID RESPONSE
            'form':form
        }
        return render(request, 'createprofile.html', context)   



# TO CREATE A MOVIE LIST FOR CHILD PROFILE WHICH IS ALSO DIFFERENT FROM MOVIES ON PARENT PROFILE     (4)
method_decorator(login_required, name='dispatch')    
class MovieList(View):      # a class to inherit from the view imported
    def get(self, request, profile_id, *args, **kwargs):    # WE PASS THE ARGUMENT(PROFILE_ID) WHEN USING TRY AND EXCEPT FUNCTION
        try:    #A TRY OUT CODE  
            profile = Profile.objects.get(uuid=profile_id)      #WE GET THE UUID THAT EQUATES THE PROFILE_ID OF A USER
            movies = Movie.objects.filter(age_limit=profile.age_limit)      #WE FILTER THROUGH MOVIE TO GET THE MOVIE AGELIMIT THATS EQUALS TO THE PROFILE AGE_LIMIT 
            if profile not in request.user.profiles.all():      #IF PROFILE IS NOT IN THE LIST OF ALL AVAILABLE PROFILES(CHILD PROFILE)
                return redirect('netflixapp:profilelist')     #TO PROFILELIST WHERE ALL PROFILES ARE LOCATED
            
            context = {
                'movies':movies                 #ELSE IF PROFILE EXISTS IN PROFILELIST GET THE MOVIE FOR THAT AGE_GRADE AND RENDER IT
            }
            return render(request, 'movielist.html', context)

        #    IF ANY ERROR OCCURS WITH THE TRY CODE, A WAY IT SHOULD BE HANDLED
        except Profile.DoesNotExist: 
            return redirect('netflixapp:profilelist') 



# TO CREATE A LOCATION THAT ENABLES OUR USER TO SEE DETAILS ABOUT A MOVIE
method_decorator(login_required, name='dispatch') 
class MovieDetail(View):         # a class to inherit from the view imported
    def get(self,request, movie_id, *args, **kwargs):
        try:
            movie = Movie.objects.get(uuid=movie_id)    #WE GET THE MOVIE BY THE UUID THAT EQUATES THE MOVIE_ID OF A USER

            context = {
                'movie':movie       # PASS THE MOVIE VAR TO THE CONTEXT
            } 
            return render(request,'moviedetail.html',context)

        #    IF ANY ERROR OCCURS WITH THE TRY CODE, A WAY IT SHOULD BE HANDLED
        except Movie.DoesNotExist:
            return redirect('netflixapp:profilelist')



# THIS VIEW IS TO MAKE THE VIDEO PLAY
method_decorator(login_required, name='dispatch') 
class PlayMovie(View):
    def get(self,request, movie_id, *args, **kwargs):       #WE PASSED THE "MOVIE_ID" ARGUMENT
        try:
            movie= Movie.objects.get(uuid=movie_id)     # TO GET THE MOVIE OBJECT WHICH UUID EQUATES THE MOVIE_ID
            movie= movie.video.values()   #WE WANT TO GET THE VALUES OF THE MOVIE OBJECT "VIDEO"           

            context = {
                'movie':list(movie)     #TO PASS A LIST OF MOVIE IN CASE ITS MORE THAN 1(e.g: SEASONAL MOVIE) TO CONTEXT
            }
            return render(request,'showmovie.html', context)

        #    IF ANY ERROR OCCURS WITH THE TRY CODE, A WAY IT SHOULD BE HANDLED
        except Movie.DoesNotExist:
            return redirect('netflixapp:profilelist')