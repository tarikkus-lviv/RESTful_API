# Generated by Django 3.0.2 on 2020-08-19 18:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social_network', '0008_like'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_date',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
