from django.shortcuts import get_object_or_404, render
from booking.models import Room, Booking


# Create your views here.
def main_page(request):
    rooms = Room.objects.all()

    context = {
        "data": "куку",
        'room_list': rooms
    }

    return render(request, "booking/room_list.html", context) 

def booking_page(request, room_id):
    room = get_object_or_404(Room, id=room_id)

    context = {
        'room': room
    }

    return render(request, 'booking/booking_page.html', context)