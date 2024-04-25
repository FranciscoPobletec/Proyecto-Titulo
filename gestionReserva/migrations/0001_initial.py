# Generated by Django 4.2.7 on 2024-04-25 21:58

from django.conf import settings
import django.contrib.auth.models
import django.contrib.auth.validators
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comerciante',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('username', models.CharField(error_messages={'unique': 'A user with that username already exists.'}, help_text='Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.', max_length=150, unique=True, validators=[django.contrib.auth.validators.UnicodeUsernameValidator()], verbose_name='username')),
                ('first_name', models.CharField(blank=True, max_length=150, verbose_name='first name')),
                ('last_name', models.CharField(blank=True, max_length=150, verbose_name='last name')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='email address')),
                ('is_staff', models.BooleanField(default=False, help_text='Designates whether the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, help_text='Designates whether this user should be treated as active. Unselect this instead of deleting accounts.', verbose_name='active')),
                ('date_joined', models.DateTimeField(default=django.utils.timezone.now, verbose_name='date joined')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidoP', models.CharField(max_length=50)),
                ('apellidoM', models.CharField(max_length=50)),
                ('contrasenia', models.CharField(max_length=30)),
                ('correo', models.EmailField(blank=True, max_length=50, null=True, unique=True)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('direccion', models.CharField(max_length=90)),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidoM', models.CharField(max_length=50)),
                ('apellidoP', models.CharField(max_length=50)),
                ('correo', models.EmailField(blank=True, max_length=50, null=True, unique=True)),
                ('contrasenia', models.CharField(max_length=30)),
                ('telefono', models.CharField(blank=True, max_length=10, null=True)),
                ('direccion', models.CharField(max_length=90)),
            ],
            options={
                'managed': True,
            },
        ),
        migrations.CreateModel(
            name='Local',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('direccion', models.CharField(max_length=90)),
                ('duenio', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Parametros',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parametro1', models.CharField(max_length=50)),
                ('parametro2', models.CharField(max_length=50)),
                ('parametro3', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Producto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('descripcion', models.CharField(blank=True, max_length=250, null=True)),
                ('cantidad', models.IntegerField(default=0)),
                ('precio', models.IntegerField(default=0)),
                ('imagen', models.ImageField(null=True, upload_to='Producto')),
                ('local', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestionReserva.local')),
            ],
        ),
        migrations.CreateModel(
            name='Reserva',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numeroOrden', models.IntegerField()),
                ('fechaInicio', models.DateField()),
                ('fechaTermino', models.DateField()),
                ('estado', models.CharField(choices=[('1', 'Solicitado'), ('2', 'En Espera'), ('3', 'Otras'), ('4', 'Retirado'), ('5', 'Cancelado Cliente'), ('6', 'Cancelado Comerciante')], default='Otras', max_length=10)),
                ('cliente', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='gestionReserva.cliente')),
                ('productos', models.ManyToManyField(to='gestionReserva.producto')),
            ],
        ),
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=50)),
                ('apellidoM', models.CharField(max_length=50)),
                ('apellidoP', models.CharField(max_length=50)),
                ('familia', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gestionReserva.cliente')),
            ],
            options={
                'managed': True,
            },
        ),
    ]
