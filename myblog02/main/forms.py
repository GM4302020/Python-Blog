
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm

class CustomChangeUserForm(UserChangeForm):

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name')

