# Generated by Django 4.2.3 on 2023-11-26 00:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0010_alter_product_category'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='photo',
            field=models.ImageField(null=True, upload_to='profile'),
        ),
    ]
