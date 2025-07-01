from django import forms
from booking.models import Booking

class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = ['name', 'email', 'phone', 'date_in', 'date_out']
        widgets = {
            'date_in': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            'date_out': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

        labels = {
            'name': "Ім'я", 'phone': 'Мобільний телефон', 'date_in': 'Дата заїзду', 'date_out': 'Дата виїзду',
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            field.widget.attrs['class'] = 'form-control'

            