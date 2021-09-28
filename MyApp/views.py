import csv

from django.http import HttpResponse
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import DetailView, ListView
from .models import User
from .templatetags.user_filters import age_validation, bizz_fuzz
# Create your views here.


class DataMixin(object):
    model = User
    fields = ['username',
              'password',
              'birth_date']
    success_url = reverse_lazy('users_list')


class UsersList(DataMixin, ListView):
    pass


class UserCreate(DataMixin, CreateView):
    pass


class UserUpdate(DataMixin, UpdateView):
    pass


class UserDelete(DataMixin, DeleteView):
    pass


class UserInfo(DataMixin, DetailView):
    pass


def download_csv(request):
    response = HttpResponse(
        content_type='text/csv',
        headers={'Content-Disposition': 'attachment; filename="Users.csv"'},
    )
    writer = csv.writer(response)
    writer.writerow(['Username', 'Birth date', 'Age validation', 'Random number', 'BizzFuzz'])
    for user in User.objects.all():
        writer.writerow([user.username, user.birth_date, age_validation(user.birth_date), user.random_number, bizz_fuzz(user.random_number)])
    return response
