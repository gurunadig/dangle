# Generated by Django 2.2.12 on 2020-06-04 11:33

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
        ('portal', '0012_auto_20200604_1702'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Assign',
            new_name='Group',
        ),
    ]