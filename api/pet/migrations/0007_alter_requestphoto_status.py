# Generated by Django 3.2.11 on 2022-11-26 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0006_auto_20221126_1832'),
    ]

    operations = [
        migrations.AlterField(
            model_name='requestphoto',
            name='status',
            field=models.CharField(blank=True, choices=[('received', 'Фото получено'), ('init', 'Форма создана'), ('filter', 'Фильтр пройден'), ('predictor', 'Ответ получен')], default='init', max_length=32, verbose_name='Статус запроса'),
        ),
    ]
