from django import forms
from .models import Accounts

class RegisterForm(forms.ModelForm):
    password= forms.CharField(label='Password', widget=forms.PasswordInput(attrs={
        'class':'form-control',
        'placeholder':'Password'
    }))
    re_password = forms.CharField(label= 'Repeat Password', widget=forms.PasswordInput(attrs={
        'class': 'form-control',
        'placeholder': 'Repeat Password'
    }))
    class Meta:
        model = Accounts
        fields = ('first_name', 'last_name', 'username', 'email', 'password')

    def clean(self):
        cleaned_data = super(RegisterForm, self).clean()
        password = cleaned_data.get('password')
        re_password = cleaned_data.get('re_password')

        if password != re_password:
            raise forms.ValidationError(
                'Password does not matched.'
            )
        email = self.cleaned_data.get('email')
        try:
            Accounts.objects.get(email=email)
            raise forms.ValidationError(
                'User with this email already exists'
            )
        except Accounts.DoesNotExist:
            pass

    def __init__(self, *args, **kargs):
        super(RegisterForm, self).__init__(*args, **kargs)
        self.fields['first_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'First name'})
        self.fields['last_name'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Last name'})
        self.fields['username'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'Username'})    
        self.fields['email'].widget.attrs.update(
            {'class': 'form-control', 'placeholder': 'example@domain.com'})