
from django.contrib.auth.forms import UserCreationForm

class CustomUserCreationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(CustomUserCreationForm, self).__init__(*args, **kwargs)
        self.fields['username'].help_text = None  # Elimina el mensaje de ayuda para el nombre de usuario

    class Meta(UserCreationForm.Meta):
        error_messages = {
            'password1': {},  # Elimina los mensajes de error predeterminados para la contraseña
        }