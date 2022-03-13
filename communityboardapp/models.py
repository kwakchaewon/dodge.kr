# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager, AbstractBaseUser
from django.utils import timezone


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
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


class AuthUserManager(BaseUserManager):
    def create_user(self, username, password, last_name, email, phone, date_birth):
        user = self.model(
            username=username,
            last_name=last_name,
            email=email,
            phone=phone,
            date_birth=date_birth,
            date_joined=timezone.now(),
            is_superuser=0,
            is_staff=0,
            is_active=1
        )

        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, password, last_name, email, phone, date_birth):
        user = self.model(
            username=username,
            password=password,
            last_name=last_name,
            email=email,
            phone=phone,
            date_birth=date_birth
        )

        user.is_superuser = 1
        user.is_staff = 1
        user.save(using=self.db)
        return user



class AuthUser(AbstractBaseUser):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150, null=True)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    phone = models.CharField(max_length=20)
    date_birth = models.DateTimeField()

    objects = AuthUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'last_name', 'phone', 'date_birth']


    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class BoardCategories(models.Model):
    category_code = models.CharField(max_length=100)
    category_type = models.CharField(max_length=100)
    category_name = models.CharField(max_length=100)
    category_desc = models.CharField(max_length=200)
    list_count = models.IntegerField(blank=True, null=True)
    authority = models.IntegerField(blank=True, null=True)
    creation_date = models.DateTimeField(blank=True, null=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'board_categories'


class BoardComment(models.Model):
    article = models.ForeignKey('Boards', models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    level = models.IntegerField(blank=True, null=True)
    content = models.CharField(max_length=300)
    reference_reply_id = models.IntegerField()
    registered_date = models.DateTimeField(blank=True, null=True, auto_now_add=True)
    last_update_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'board_comment'


class Boards(models.Model):
    category = models.ForeignKey(BoardCategories, models.DO_NOTHING)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    title = models.CharField(max_length=300)
    content = models.TextField()
    registered_date = models.DateTimeField(blank=True, null=True)
    last_update_date_date = models.DateTimeField(blank=True, null=True)
    view_count = models.PositiveIntegerField(default=0)
    image = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'boards'

    @property
    def updateViewcount(self):
        self.view_count = self.view_count + 1
        self.save()


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
