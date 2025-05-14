from django import forms
from .models import Event

class EventForm(forms.ModelForm):
    """
    Form for creating and updating events by organizations.
    """
    class Meta:
        model = Event
        fields = ['title', 'description', 'date', 'location', 'image', ]
        widgets = {
            'date': forms.DateTimeInput(attrs={'type': 'datetime-local'}, format='%Y-%m-%dT%H:%M'),
            'description': forms.Textarea(attrs={'rows': 4}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # If you're using Bootstrap or another CSS framework, you can add classes here
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control mb-2'
        self.fields['date'].input_formats = ('%Y-%m-%dT%H:%M',)
