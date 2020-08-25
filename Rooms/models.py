from django.db import models
from django.contrib.auth.models import User
# from django.utils import timezone


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

class RoomClean(models.Model):
    Date = models.DateTimeField(auto_now_add=True, blank=True)
    Roomnumber = models.CharField (max_length=140, default='')
    Clean_Under_Bedding = models.BooleanField()
    Insects_Check = models.BooleanField()
    replace_Bedspread = models.BooleanField()
    replace_Pillow_Covers = models.BooleanField()
    Clean_Replace_Blankets = models.BooleanField()
    Clean_Night_Stand = models.BooleanField()
    Clean_Windows = models.BooleanField()
    Clean_Curtain = models.BooleanField()
    Clean_Mirrors = models.BooleanField()
    Hanger_Regular = models.CharField (max_length=140, default='')
    Hanger_clipper = models.CharField (max_length=140, default='')
    Clean_Tv_Furniture = models.BooleanField()
    Clean_Tv_Under_Furniture = models.BooleanField()
    Clean_Tv_Furniture_drawers = models.BooleanField()
    Clean_Desk_Furniture = models.BooleanField()
    Clean_Desk_Chair = models.BooleanField()
    Clean_Phone = models.BooleanField()
    Check_Phone = models.BooleanField()
    Clean_Tv = models.BooleanField()
    Check_Tv = models.BooleanField()
    Check_Remote = models.BooleanField()
    Clean_Microwave = models.BooleanField()
    Clean_Fridge = models.BooleanField()
    Check_Microwave = models.BooleanField()
    Check_Fridge = models.BooleanField()
    Clean_AC = models.BooleanField()
    Check_AC = models.BooleanField()
    Clean_Floor = models.BooleanField()
    Ice_Bucket = models.BooleanField()
    Water_Cups = models.BooleanField()
    Marketing_Material = models.BooleanField()
    Clean_Toilet = models.BooleanField()
    Clean_Shower_Curtain = models.BooleanField()
    Clean_Shower_Head = models.BooleanField()
    Clean_Bathtub = models.BooleanField()
    Clean_Sink = models.BooleanField()
    Clean_Venity = models.BooleanField()
    Clean_Venity_Mirror = models.BooleanField()
    Toilet_Paper = models.BooleanField()
    Bath_Towel = models.CharField (max_length=6, default='')
    Hand_Towel = models.CharField (max_length=6, default='')
    Wash_Cloth = models.CharField (max_length=6, default='')
    Bath_Mate = models.CharField (max_length=140, default='')
    Bath_Soap = models.CharField (max_length=140, default='')
    Clean_Bathroom_Floor = models.BooleanField()
    Check_Smoke_Alarm = models.BooleanField()
    Check_Latch = models.BooleanField()
    Check_Lock = models.BooleanField()
    Check_Door_Stickers = models.BooleanField()
    Comment= models.CharField(max_length=140)

    objects = models.Manager()


def __str__(self): 
        return self.roomnumber


class  Test(models.Model):
    comment = models.CharField(max_length=140)
    comment1 = models.CharField(max_length=140)
    comment2 = models.CharField(max_length=140, default="")
    def __str__(self):
     return self.comment    
    




    