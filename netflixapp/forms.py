#WE CREATED FORMS.PY TO WORK WITH THE CREATE VIEW IN VIEWS

from django.forms import ModelForm  #mandatory when using a form in order to inherit it as an attribute
from .models import Profile   #Our model


class ProfileForm(ModelForm):
    class Meta:     #To enble us use the model we want to interact with
        model = Profile
        exclude = ['uuid']      #In case we want to exclude any fild in our models
                                #whereas I'm taking only the name and age_linit from our profile Model

