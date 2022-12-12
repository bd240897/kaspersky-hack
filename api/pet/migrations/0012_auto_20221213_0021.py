# Generated by Django 3.2.11 on 2022-12-12 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pet', '0011_auto_20221213_0020'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diseases',
            name='more_information',
            field=models.TextField(blank=True, max_length=10000, null=True, verbose_name='Подробное описание'),
        ),
        migrations.AlterField(
            model_name='quickrequestphoto',
            name='status',
            field=models.CharField(blank=True, choices=[('received', 'Фото получено'), ('init', 'Форма создана'), ('predictor', 'Ответ получен'), ('filter', 'Фильтр пройден')], default='init', max_length=32, verbose_name='Статус запроса'),
        ),
        migrations.AlterField(
            model_name='requestphoto',
            name='status',
            field=models.CharField(blank=True, choices=[('received', 'Фото получено'), ('init', 'Форма создана'), ('predictor', 'Ответ получен'), ('filter', 'Фильтр пройден')], default='init', max_length=32, verbose_name='Статус запроса'),
        ),
    ]