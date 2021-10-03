from django.contrib.auth import get_user_model
from django.urls import reverse_lazy


User = get_user_model()


class DataMixin:
    model = User
    fields = ['username',
              'password',
              'birth_date']
    success_url = reverse_lazy('users_list')
