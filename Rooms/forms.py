from django import forms
from Rooms.models import deepclean

class deepcleanlists (forms.ModelForm):
    

    class Meta: 
        model = deepclean
        fields = '__all__'
 