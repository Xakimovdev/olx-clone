# Generated by Django 5.0.2 on 2024-02-19 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0007_remove_post_json'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='json',
            field=models.JSONField(blank=True, null=True),
        ),
    ]
