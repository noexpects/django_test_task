# Generated by Django 3.2.7 on 2021-09-27 16:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0004_auto_20210927_1913'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(help_text='Year-Month-Day'),
        ),
        migrations.AlterField(
            model_name='user',
            name='random_number',
            field=models.PositiveIntegerField(default=12, editable=False),
        ),
    ]