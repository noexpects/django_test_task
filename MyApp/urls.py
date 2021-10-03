from django.urls import path
from .views import UserCreate, UserUpdate, UserDelete, UserInfo, UsersList, DownloadCSV

urlpatterns = [
    path('', UsersList.as_view(), name='users_list'),
    path('create_user', UserCreate.as_view(), name='user_create'),
    path('update_user/<pk>', UserUpdate.as_view(), name='user_update'),
    path('delete_user/<pk>', UserDelete.as_view(), name='user_delete'),
    path('user_info/<pk>', UserInfo.as_view(), name='user_details'),
    path('download', DownloadCSV.as_view(), name='users_download'),
]
