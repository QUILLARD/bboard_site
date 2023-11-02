from django.contrib.auth.models import AbstractUser
from django.db import models


class AdvUser(AbstractUser):
    is_activated = models.BooleanField(default=True, db_index=True, verbose_name='Активирован аккаунт?')
    send_messages = models.BooleanField(default=True, verbose_name='Слать оповещения о новых комментариях?')

