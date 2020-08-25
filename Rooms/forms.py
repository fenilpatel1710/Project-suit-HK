from django import forms
from Rooms.models import RoomClean

class Roomcleanlists (forms.ModelForm):
    

    class Meta: 
        model = RoomClean
        fields = '__all__'
 