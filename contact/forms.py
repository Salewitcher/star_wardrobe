from django import forms
from .models import ContactMessage

class ContactMessageForm(forms.ModelForm):
    class Meta:
        model = ContactMessage
        fields = ['full_name', 'email', 'phone_number', 'message']
        widgets = {
            'message': forms.Textarea(attrs={'rows': 5}),
        }
