from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegularUserSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'first_name', 'last_name')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'regular'
        if commit:
            user.save()
        return user
    
class OrganizationSignUpForm(UserCreationForm):
    organization_name = forms.CharField(max_length=255)
    logo = forms.ImageField(required=False, label='Company Logo')

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'organization_name', 'logo')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.user_type = 'organization'
        
        if commit:
            user.save()
        return user
    

