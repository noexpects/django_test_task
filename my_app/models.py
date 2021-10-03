import random
from django.db import models
from django.shortcuts import reverse
from django.contrib.auth.models import AbstractUser


def get_rnd():
    return random.randint(1, 100)


class User(AbstractUser):
    birth_date = models.DateField(help_text='Year-Month-Day')
    random_number = models.PositiveIntegerField(editable=False, default=get_rnd)

    def get_absolute_url(self):
        return reverse('users_list')