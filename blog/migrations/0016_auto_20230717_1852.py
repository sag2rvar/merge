# Generated by Django 3.2.20 on 2023-07-17 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0015_auto_20230717_0657'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='featured_image',
            field=models.ImageField(blank=True, null=True, upload_to='featured_images/'),
        ),
        migrations.AddField(
            model_name='post',
            name='thumbnail_image',
            field=models.ImageField(blank=True, null=True, upload_to='thumbnail_images/'),
        ),
    ]
