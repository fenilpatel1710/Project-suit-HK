from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.

room_type = (
    ("king smoking","KS"),
    ("king nonsmoking", "KNS"),
    ("king nonsmoking handicap", "KNSH"),
    ("king smoking handicap", "KSH"),
    ("queen smoking","QS"),
    ("queen nonsmoking", "QNS"),
    ("queen nonsmoking handicap", "QNSH"),
    ("queen smoking handicap", "QSH"),
    
)

room_floor = (
    ("1st floor", "1st floor"),
    ("2nd floor", "2nd floor"),
    ("3rd floor", "3rd floor"),

)

room_status = (
    ("clean", "clean"),
    ("dirty", "dirty"),
    ("maintenance", "maintenance"),



)


class roomtype (models.Model):
    room_type =  models.CharField(max_length=140, choices = room_type, default="KS")
    def __str__ (self):
        return self.room_type


class roomfloor (models.Model):
    room_floor = models.CharField(max_length=50,choices = room_floor, default="1st floor")
    def __str__ (self):
        return self.room_floor
    

class roomstatus (models.Model):
    room_status = models.CharField(max_length=50,choices = room_status, default="maintenance")
    def __str__ (self):
        return self.room_status


class room(models.Model):
    room_number = models.CharField(max_length=140, default='')
    room_type =  models.CharField(max_length=140, choices = room_type, default="KS")
    room_floor = models.CharField(max_length=50,choices = room_floor, default="1st floor")
    room_status = models.CharField(max_length=50,choices = room_status, default="maintenance")

    objects = models.Manager() 

    class Meta:
        ordering = ['room_number']

    def __str__ (self):
        return self.room_number

class Roomclean(models.Model):
    Date = models.DateTimeField(auto_now_add=True, blank=True)
    Roomnumber = models.CharField (max_length=140, default='')
    Clean_Under_Bedding = models.BooleanField()
    Insects_Check = models.BooleanField()
    replace_Bedspread = models.BooleanField()
    replace_Pillow_Covers = models.BooleanField()
    Clean_Replace_Blankets = models.BooleanField()
    Comment_For_Bedding= models.CharField(max_length=140)
    Clean_Windows = models.BooleanField()
    Clean_Mirrors = models.BooleanField()

    objects = models.Manager()


def __str__(self): 
        return self.roomnumber


class  Test(models.Model):
    comment = models.CharField(max_length=140)
    comment1 = models.CharField(max_length=140)
    def __str__(self):
     return self.comment    
    




    