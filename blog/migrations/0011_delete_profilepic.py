# Generated by Django 4.2.2 on 2023-07-25 17:24

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_remove_profilepic_date_added_and_more'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ProfilePic',
        ),
    ]
