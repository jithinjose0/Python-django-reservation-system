from django import forms
from myapp.models import Book, bookingform

class members(forms.ModelForm):
    
    class Meta:
        model=bookingform
        fields='__all__'
class Bookform(forms.ModelForm):
    
	class Meta:
		model = Book
		fields = ('payment_type',)