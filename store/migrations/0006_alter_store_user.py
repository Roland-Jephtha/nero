# Generated by Django 4.2.3 on 2023-11-21 16:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0005_store_paid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='store',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='store', to=settings.AUTH_USER_MODEL),
        ),
    ]