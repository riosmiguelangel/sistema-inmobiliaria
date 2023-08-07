# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    id = models.BigAutoField(primary_key=True)
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class Propiedades(models.Model):
    codigo_externo = models.CharField(max_length=45)
    codigo_interno = models.CharField(max_length=45)
    tipo_operacion = models.ForeignKey('TipoOperacion', models.DO_NOTHING, db_column='tipo_operacion', related_name='operacion' )
    tipo_propiedad = models.ForeignKey('TipoPropiedad', models.DO_NOTHING, db_column='tipo_propiedad')
    tipo_provincia = models.ForeignKey('TipoProvincia', models.DO_NOTHING, db_column='tipo_provincia')
    tipo_barrio = models.ForeignKey('TipoBarrio', models.DO_NOTHING, db_column='tipo_barrio')
    tipo_ambiente = models.ForeignKey('TipoAmbientes', models.DO_NOTHING, db_column='tipo_ambiente')
    valor = models.IntegerField()
    descripcion = models.TextField(db_collation='utf8mb3_swedish_ci')
    calle = models.CharField(max_length=45)
    altura = models.SmallIntegerField()
    piso = models.CharField(max_length=3)
    depto = models.CharField(max_length=3)
    torre = models.CharField(max_length=10)
    fecha_alta = models.DateTimeField()
    moneda = models.CharField(max_length=10)
    reservado = models.IntegerField()
    #imagenP = models.ForeignKey(ImagenPropiedad, on_delete=models.CASCADE,related_name='imagenP')
    
    class Meta:
        managed = False
        db_table = 'propiedades'



class TipoAmbientes(models.Model):
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipo_ambientes'

    def __str__(self):
        return self.descripcion


class TipoBarrio(models.Model):
    id_provincia = models.PositiveIntegerField()
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipo_barrio'
        unique_together = (('id', 'id_provincia'),)

    def __str__(self):
        return self.descripcion


class TipoOperacion(models.Model):
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipo_operacion'
    
    def __str__(self):
        return self.descripcion


class TipoPropiedad(models.Model):
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipo_propiedad'

    def __str__(self):
        return self.descripcion


class TipoProvincia(models.Model):
    descripcion = models.CharField(max_length=45)

    class Meta:
        managed = False
        db_table = 'tipo_provincia'

    def __str__(self):
        return self.descripcion


