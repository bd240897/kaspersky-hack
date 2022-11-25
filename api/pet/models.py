from django.db import models
from django.contrib.auth.models import User
import requests as requests_lib
from django.urls import reverse
from django.utils.timezone import now

class Profile(models.Model):
    """Профиль юзера"""

    first_name = models.CharField(verbose_name="Имя", max_length=100, blank=True, null=True)
    second_name = models.CharField(verbose_name="Фамилия", max_length=100, blank=True, null=True)
    third_name = models.CharField(verbose_name="Отчество", max_length=100, blank=True, null=True)
    avatar = models.ImageField(verbose_name="Аватарка", upload_to='core/profile', default='core/profile/avatar_default.png')
    user = models.OneToOneField(User, verbose_name="Юзер", on_delete=models.CASCADE, related_name='pet_profile_user', db_index=True)
    active = models.BooleanField(verbose_name="Статус", default=True)
    date_creation = models.DateTimeField(verbose_name="Дата создания", default=now, editable=False)

    class Meta:
        verbose_name = 'Профиль владельца'
        verbose_name_plural = 'Профили владельца'

    def __str__(self):
        return str(', '.join((self.first_name, self.second_name, self.third_name)))


class Pet(models.Model):
    """Профиль питомца"""

    owner = models.ForeignKey(User, verbose_name="Владелец", on_delete=models.CASCADE, related_name='pet_owner', db_index=True)
    name = models.CharField(verbose_name="Имя", max_length=100, blank=True, null=True)
    avatar = models.ImageField(verbose_name="Аватарка", upload_to='pet/profile', default='core/profile/avatar_default.png')
    age = models.CharField(verbose_name="Имя", max_length=100, blank=True, null=True) # TODO
    weight = models.CharField(verbose_name="Имя", max_length=100, blank=True, null=True) # TODO
    breed = models.CharField(verbose_name="Имя", max_length=100, blank=True, null=True)


class Diseases(models.Model):
    """Список болезней"""

    name = models.CharField(verbose_name="Имя", max_length=100, blank=True, null=True)
    description = models.CharField(verbose_name="Имя", max_length=100, blank=True, null=True)

class RequestPhoto(models.Model):
    """Предсказания длч питомца"""

    pet = models.ForeignKey(Pet, verbose_name="Питомец", on_delete=models.CASCADE, related_name='prediction_photo_pet', db_index=True)
    photo = models.ImageField(verbose_name="Экскоременты", upload_to='prediction_photo/profile') # TODO
    date_creation = models.DateTimeField(verbose_name="Дата создания", default=now, editable=False)
    diseases = models.ManyToManyField(Diseases)

class RequestPoll(models.Model):
    """Предсказания длч питомца"""

    pet = models.ForeignKey(Pet, verbose_name="Питомец", on_delete=models.CASCADE, related_name='prediction_poll_pet', db_index=True)
    photo = models.ImageField(verbose_name="Экскоременты", upload_to='prediction_photo/profile') # TODO
    date_creation = models.DateTimeField(verbose_name="Дата создания", default=now, editable=False)
    diseases = models.ManyToManyField(Diseases)

