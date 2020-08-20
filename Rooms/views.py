from django.shortcuts import render
from django.shortcuts import HttpResponse
from .models import room
from .models import deepclean
from .forms import deepcleanlists

# Create your views here.


def index(request):

     return render(request, 'Rooms/Rooms.html')

def room_list(request):

     
     context = {
        'roomList' : room.objects.all()
     }
     return render(request, 'Rooms/AllRooms.html', context)

     
def room_detail(request,room_number):


     context_dict = {
        'roomDetail' : room.objects.get(room_number = room_number)
     }
     
     
     if request.method == 'POST':
          form = deepcleanlists(request.POST)
          if form.is_valid():
               form.save()
          else:
               return HttpResponse("your form is wrong")

               
     else:
          form=deepcleanlists()     
                      

     context_dict.update({"form":form})
     
     return render(request,'Rooms/RoomDetail.html', context=context_dict)

def room_detai(request,room_number,RoomDetail):


     context_dict = {
        'roomDetail' : room.objects.get(room_number = room_number)
     }
     
     
     if request.method == 'POST':
          form = deepcleanlists(request.POST)
          if form.is_valid():
               form.save()
          else:
               return HttpResponse("your form is wrong")

               
     else:
          form=deepcleanlists()       
                      
               
                   

     context_dict.update({"form":form})
     
     
     return render(request,'Rooms/RoomDetail.html', context=context_dict)     

def room_status(request,room_status):


     context = {
        'roomList' : room.objects.filter(room_status=room_status).values()
     }
     
     return render(request,'Rooms/RoomStatus.html', context)     


def Detail_Report(request):

     DetailReport = deepclean.objects.all()

     return render(request, 'Rooms/Report.html', {'DetailReport':DetailReport})


     






     