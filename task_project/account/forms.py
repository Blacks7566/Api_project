from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from account.models import User

class CustomUserCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['email','name','phone','gender']

class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = User
        fields = ['email','name','phone','gender']