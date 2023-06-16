from typing import Any
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(UserCreateForm, self).__init__(*args, **kwargs)

        for fildname in ['username', 'password1', 'password2']:
            self.fields[fildname].help_text = None
            self.fields[fildname].widget.attrs.update({'class': 'form-control'})