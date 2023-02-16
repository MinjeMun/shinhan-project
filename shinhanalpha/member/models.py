from django.db import models

# Create your models here.
from django.contrib.auth.models import AbstractUser

# Create your models here.

class Member(AbstractUser):
    phone = models.CharField(max_length=32, null=True, blank=True, verbose_name='전화번호')
    propensity = models.CharField(max_length=32, null=True, blank)

    class Meta:
        db_table = 'shinhan_member'
        verbose_name = '회원'
        verbose_name_plural = '회원'