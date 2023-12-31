# Generated by Django 3.2.20 on 2023-07-18 12:13

import autoslug.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0018_alter_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='slug',
            field=autoslug.fields.AutoSlugField(editable=False, populate_from='title', unique=True),
        ),
    ]
