from django.db import models
from django.contrib.auth.models import User


class TypeRoom(models.Model):
    name = models.CharField(verbose_name="Тип кімнати:")
    description = models.TextField(null=True, blank=True, verbose_name="Опис кімнати:")

    def __str__(self):
        return f'{self.name}'
    

    class Meta():
        verbose_name = "Тип кімнати"         # Назва в однині в адмінці
        verbose_name_plural = "Тип кімнат"  # Назва в множині


class Room(models.Model):
    type_room = models.ForeignKey(TypeRoom, on_delete=models.CASCADE, related_name='rooms', verbose_name="Тип кімнати:")
    name = models.CharField(max_length=100, verbose_name="Номер кімнати:")
    picture = models.ImageField(upload_to='Rooms', null=True)
    price = models.IntegerField()
    description = models.TextField(null=True, blank=True)
    places = models.IntegerField(default=1)

    def __str__(self):
        return f'Кімната: {self.name}, ціна: {self.price}.'
    

    class Meta():
        verbose_name = "Кімната"         # Назва в однині в адмінці
        verbose_name_plural = "Кімнати"  # Назва в множині


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE, related_name='bookings')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bookings')
    name = models.CharField(max_length=100)
    email = models.EmailField()
    date_in = models.DateTimeField()
    date_out = models.DateTimeField()
    creation_date = models.DateTimeField(auto_now_add=True)
    phone = models.CharField(max_length=20)


    def __str__(self):
        return f'Бронювання:{self.room}, Дата заїзду:{self.date_in}, Дата виїзду:{self.date_out}.'
    

    class Meta():
        verbose_name = "Бронювання"         # Назва в однині в адмінці
        verbose_name_plural = "Бронювання"  # Назва в множині
    

