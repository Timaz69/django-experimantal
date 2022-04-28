from django import forms
from django.core import validators
from appTwo.models import Users, UserProfilInfo
from django.contrib.auth.models import User

class FormName(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    email = forms.EmailField(widget=forms.TextInput(attrs={'class':'form-control'}))
    verify_email = forms.EmailField(label='Enter email again', widget=forms.EmailInput(attrs={'class':'form-control'}))
    text = forms.CharField(widget=forms.Textarea(attrs={'class':'form-control'}))
    botcatcher = forms.CharField(required=False, widget=forms.HiddenInput, validators=[validators.MaxLengthValidator(0)])

    def clean(self):
        all_data_clean = super().clean()
        email = all_data_clean['email']
        vemail = all_data_clean['verify_email']

        if email != vemail:
            raise forms.ValidationError("MAKE SURE YOU'RE EMAIL MATCH!")

class UserForm(forms.ModelForm):
    class Meta():
        model = Users
        fields = '__all__'
        widgets= {
            'first_name': forms.TextInput(attrs={'class':'form-control', 'placeholder':'This is placeholder stuff'}),
            'last_name': forms.TextInput(attrs={'class':'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class UserFormulaire(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    class Meta():
        model = User
        fields = ('username', 'email', 'password')
        widgets = {
        'username': forms.TextInput(attrs={'class': 'form-control'}),
        'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }

class UserProfilForm(forms.ModelForm):
    class Meta():
        model=UserProfilInfo
        fields = ('portfolio_site', 'profil_pic')
        widgets = {
        'portfolio_site': forms.URLInput(attrs={'class': 'form-control'}),
        'profil_pic': forms.FileInput(attrs={'class': 'form-control'}),
        }
