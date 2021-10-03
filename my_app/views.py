import csv
from .mixins import DataMixin
from django.http import HttpResponse
from django.views.generic.edit import CreateView, UpdateView, DeleteView, View
from django.views.generic import DetailView, ListView
from django.contrib.auth import get_user_model
from .templatetags.user_filters import age_validation, bizz_fuzz
# Create your views here.
User = get_user_model()


class UsersList(DataMixin, ListView):
    paginate_by = 6


class UserCreate(DataMixin, CreateView):
    pass


class UserUpdate(DataMixin, UpdateView):
    pass


class UserDelete(DataMixin, DeleteView):
    pass


class UserInfo(DataMixin, DetailView):
    pass


class DownloadCSV(View):
    def get(self, request, *args, **kwargs):
        response = HttpResponse(
            content_type='text/csv',
            headers={'Content-Disposition': 'attachment; filename="Users.csv"'},
        )
        writer = csv.writer(response)
        writer.writerow(['Username', 'Birth date', 'Age validation', 'Random number', 'BizzFuzz'])
        for user in User.objects.all():
            writer.writerow([user.username,
                             user.birth_date,
                             age_validation(user.birth_date),
                             user.random_number,
                             bizz_fuzz(user.random_number)])
        return response