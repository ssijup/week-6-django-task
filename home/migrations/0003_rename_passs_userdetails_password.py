# Generated by Django 4.1.4 on 2023-01-19 03:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_rename_password_userdetails_passs'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userdetails',
            old_name='passs',
            new_name='password',
        ),
    ]
