# Generated by Django 4.2.3 on 2023-11-26 02:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_profile_photo'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='number',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='business_name',
            field=models.CharField(max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='email',
            field=models.EmailField(max_length=255, null=True),
        ),
    ]
