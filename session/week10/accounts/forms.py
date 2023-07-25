from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm


class UserBasedFrom(forms.ModelForm):
    class Meta:
        model = get_user_model()
        fields = '__all__'


class UserCreateForm(UserBasedFrom):
    password2 = forms.CharField(widget=forms.PasswordInput)

    class Meta(UserBasedFrom.Meta):
        fields = ['username', 'email', 'phone', 'password']


class SignupForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = ['username', 'email']
