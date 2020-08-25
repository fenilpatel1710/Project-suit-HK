from django import forms
from Rooms.models import Roomclean

class Roomcleanlists (forms.ModelForm):
    

    class Meta: 
        model = Roomclean
        fields = '__all__'
 