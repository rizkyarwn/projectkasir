from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='user_profile')
    nama = models.CharField(max_length=50)
    nomor_hp = models.IntegerField()
    alamat = models.TextField()

    STATUS_CHOICES = (
        ('admin', 'Admin'),
        ('kasir', 'Kasir'),
        ('koki', 'Koki'),
        ('pelayan', 'Pelayan')
    )
    status = models.CharField(max_length=10, choices=STATUS_CHOICES)