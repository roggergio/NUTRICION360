from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MinLengthValidator
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError

# Create your models here.
class MyAccountManager(BaseUserManager):
    def create_user(self, first_name, last_name, username, email, password=None):
        if not email:
            raise ValueError('el usuario debe tener un email')
        if not username:
            raise ValueError('el usuario debe tener un username')
        user = self.model(
            email=self.normalize_email(email),
            username=username,
            first_name=first_name,
            last_name=last_name,
        )
        user.set_password(password)
        user.save(using=self._db)

        return user
    def create_superuser(self, first_name, last_name, email, username, password):
        user = self.create_user(
            email = self.normalize_email(email),
            username = username,
            password = password,
            first_name = first_name,
            last_name = last_name,
        )
        user.is_admin = True
        user.is_active = True
        user.is_staff = True
        user.is_superadmin = True
        user.save(using=self._db)
        return user

class Account(AbstractBaseUser):
    first_name = models.CharField(
        max_length=50,
        validators=[MinLengthValidator(3)]  # Validador para la longitud mínima
    )
    last_name = models.CharField(max_length=50)
    username = models.CharField(max_length=50, unique=True)
    email = models.EmailField(max_length=100, unique=True)
    phone_number = models.CharField(
    max_length=10,
    validators=[RegexValidator(regex=r'^\+?1?\d{9,11}$', message="El número debe tener entre 9 y 15 dígitos y puede incluir '+' al inicio.")]
)

                                            #campos atributos de django
    # fecha
    date_joined = models.DateTimeField(auto_now_add=True)

    #ultima conexion
    last_login = models.DateTimeField(auto_now_add=True)

    #fecha de corte 
    expiration_date = models.DateTimeField(auto_now_add=True)

    #es administrador
    is_admin = models.BooleanField(default=False)

    # es parte del equipo de la plataforma
    is_staff = models.BooleanField(default=False)

    #esta activo
    is_active = models.BooleanField(default=False)

    #es superadmin
    is_superadmin = models.BooleanField(default=False)

    #para iniciar sesion con email y no con nombre
    USERNAME_FIELD='email'

    #campos requeridos dentro de formulario de registro
    REQUIRED_FIELDS=['username', 'first_name', 'last_name']

    objects=MyAccountManager()

    def __str__(self):

        return self.email

    def has_perm (self, perm, obj=None):
        return self.is_admin

    def has_module_perms (self, add_label):
        return True
