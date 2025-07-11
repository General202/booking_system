from django.contrib import admin
from django.urls import path
from booking import views

urlpatterns = [
    path('', views.main_page, name="main"),
    path('room/<int:room_id>', views.booking_page, name='booking_page'),
    path('type_room/<int:type_id>', views.type_room_page, name='type_room_page')
] 