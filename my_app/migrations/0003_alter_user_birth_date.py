# Generated by Django 3.2.7 on 2021-10-03 23:24

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('my_app', '0002_alter_user_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='birth_date',
            field=models.DateField(default=django.utils.timezone.now, help_text='Year-Month-Day'),
            preserve_default=False,
        ),
    ]
