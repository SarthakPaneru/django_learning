# Generated by Django 3.2.6 on 2021-09-15 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auth_user', '0003_remove_author_password'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='profile_pic',
            field=models.ImageField(blank=True, null=True, upload_to='images'),
        ),
    ]
