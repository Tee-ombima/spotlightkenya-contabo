# Generated by Django 4.0.8 on 2022-10-30 08:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_remove_user_date_joined_alter_user_first_name_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='phone_number',
        ),
    ]
