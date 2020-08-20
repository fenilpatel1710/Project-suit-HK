from django.urls import path
from django.urls import path,include
from. import views

urlpatterns = [

    path('',views.index),
    path('AllRooms',views.room_list),
    path('RoomDetail/<int:room_number>',views.room_detail),
    path('RoomStatus/<str:room_status>',views.room_status),
    path('RoomStatus/<slug:RoomDetail>/<int:room_number>',views.room_detai),
    path('Report',views.Detail_Report) 
]