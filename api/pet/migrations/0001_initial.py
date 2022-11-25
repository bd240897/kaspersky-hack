# Generated by Django 3.2.11 on 2022-11-25 11:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Diseases',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя')),
                ('description', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя')),
            ],
        ),
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя')),
                ('avatar', models.ImageField(default='core/profile/avatar_default.png', upload_to='pet/profile', verbose_name='Аватарка')),
                ('age', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя')),
                ('weight', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя')),
                ('breed', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pet_owner', to=settings.AUTH_USER_MODEL, verbose_name='Владелец')),
            ],
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Имя')),
                ('second_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Фамилия')),
                ('third_name', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество')),
                ('avatar', models.ImageField(default='core/profile/avatar_default.png', upload_to='core/profile', verbose_name='Аватарка')),
                ('active', models.BooleanField(default=True, verbose_name='Статус')),
                ('date_creation', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Дата создания')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='pet_profile_user', to=settings.AUTH_USER_MODEL, verbose_name='Юзер')),
            ],
            options={
                'verbose_name': 'Профиль',
                'verbose_name_plural': 'Профили',
            },
        ),
        migrations.CreateModel(
            name='PredictionPoll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='prediction_photo/profile', verbose_name='Экскоременты')),
                ('date_creation', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Дата создания')),
                ('diseases', models.ManyToManyField(to='pet.Diseases')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prediction_poll_pet', to='pet.pet', verbose_name='Питомец')),
            ],
        ),
        migrations.CreateModel(
            name='PredictionPhoto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='prediction_photo/profile', verbose_name='Экскоременты')),
                ('date_creation', models.DateTimeField(default=django.utils.timezone.now, editable=False, verbose_name='Дата создания')),
                ('diseases', models.ManyToManyField(to='pet.Diseases')),
                ('pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='prediction_photo_pet', to='pet.pet', verbose_name='Питомец')),
            ],
        ),
    ]