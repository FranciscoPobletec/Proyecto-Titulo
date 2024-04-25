
from django import forms
from gestionReserva.models import Comerciante, Local, Producto


class ComercianteForm(forms.ModelForm):
    class Meta:
        model = Comerciante
        fields = ['nombre', 'apellidoM', 'apellidoP','contrasenia', 'correo', 'telefono', 'direccion']
        # Define los widgets para cada campo del formulario, incluyendo placeholders y renderizado de contraseñas
        widgets = {
            'nombre': forms.TextInput(attrs={'placeholder': 'Ingrese el nombre'}),
            'apellidoM': forms.TextInput(attrs={'placeholder': 'Ingrese el apellido materno'}),
            'apellidoP': forms.TextInput(attrs={'placeholder': 'Ingrese el apellido paterno'}),
            'contrasenia': forms.PasswordInput(render_value=True, attrs={'placeholder': 'Ingrese la contraseña'}),
            'correo': forms.EmailInput(attrs={'placeholder': 'Ingrese el correo electrónico'}),
            'telefono': forms.TextInput(attrs={'placeholder': 'Ingrese el teléfono'}),
            'direccion': forms.TextInput(attrs={'placeholder': 'Ingrese la dirección'}),
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Personaliza las etiquetas de los campos del formulario
        self.fields['nombre'].label = 'Nombre'
        self.fields['apellidoM'].label = 'Apellido materno'
        self.fields['apellidoP'].label = 'Apellido paterno'
        self.fields['contrasenia'].label = 'Contraseña'
        self.fields['correo'].label = 'Correo electrónico'
        self.fields['telefono'].label = 'Teléfono'
        self.fields['direccion'].label = 'Dirección'

    def save(self, commit=True):
        # Guarda una instancia del modelo Comerciante con los datos del formulario
        instance = super().save(commit=False)
        # Asigna los datos del formulario a los campos correspondientes del modelo Comerciante
        instance.first_name = self.cleaned_data['nombre']
        instance.last_name = self.cleaned_data['apellidoM']
        instance.email = self.cleaned_data['correo']
        # Genera un nombre de usuario a partir del correo electrónico
        instance.username = instance.email.split('@')[0]
        # Asigna la contraseña utilizando el método set_password para encriptarla
        instance.set_password(self.cleaned_data['contrasenia'])
        if commit:
            instance.save()  # Guarda la instancia en la base de datos si commit es True
        return instance  # Devuelve la instancia del modelo Comerciante


class LocalForm(forms.ModelForm):
    class Meta:
        model = Local
        fields = ['nombre', 'direccion', 'duenio']


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion','cantidad', 'precio', 'imagen', 'local']
