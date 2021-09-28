# Generated by Django 3.2.7 on 2021-09-27 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(auto_now_add=True, help_text='Year/Month/Day'),
        ),
        migrations.AlterField(
            model_name='user',
            name='random_number',
            field=models.PositiveIntegerField(default=1),
        ),
    ]