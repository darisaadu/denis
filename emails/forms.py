from django import forms
from .models import EmailEntry

class EmailEntryUpdateForm(forms.ModelForm):
    
    class Meta:
        model = EmailEntry
        fields = ['name', 'bio', 'email']


class EmailEntryForm(forms.ModelForm):
    email = forms.EmailField(label='',
        widget=forms.EmailInput(
            attrs={
                "placeholder": "Your email",
                "class": "form-control"
            }
        )
    )
    
    class Meta:
        model = EmailEntry
        fields = ['email']


    def clean_email(self):
        email = self.cleaned_data.get('email')
        qs = EmailEntry.objects.filter(email__iexact=email)
        if qs.exists():
            raise forms.ValidationError("Thank you, you have already registered.")
        return email