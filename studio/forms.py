from django import forms
from .models import Commission

class CommissionForm(forms.ModelForm):
    class Meta:
        model = Commission
        fields = [
            'name',
            'email',
            'whatsapp',
            'style',
            'size',
            'subjects',
            'description',
            'extra',
            'deadline',
        ]
        widgets = {
            'name': forms.TextInput(attrs={
                'placeholder': 'Your full name'
            }),
            'email': forms.EmailInput(attrs={
                'placeholder': 'your@email.com'
            }),
            'whatsapp': forms.TextInput(attrs={
                'placeholder': '+234 000 000 0000'
            }),
            'description': forms.Textarea(attrs={
                'placeholder': 'Describe what you want...',
                'rows': 5
            }),
            'extra': forms.Textarea(attrs={
                'placeholder': 'Any extra requests?...',
                'rows': 3
            }),
            'deadline': forms.DateInput(attrs={
                'type': 'date'
            }),
        }