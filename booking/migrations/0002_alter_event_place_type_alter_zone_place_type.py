# Generated by Django 4.2.6 on 2023-11-24 10:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('booking', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='place_type',
            field=models.CharField(choices=[('restaurant', 'Ресторан'), ('cafe', 'Кафе'), ('cabin', 'Кабинка')], max_length=50),
        ),
        migrations.AlterField(
            model_name='zone',
            name='place_type',
            field=models.CharField(choices=[('cafe', 'Кафе'), ('cabin', 'Кабинка')], max_length=50),
        ),
    ]