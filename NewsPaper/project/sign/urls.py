from django.urls import path
from .views import upgrade_account

urlpatterns = [
    path('upgrade/', upgrade_account, name='sign_upgrade')
]