# Generated by Django 3.0.5 on 2020-06-24 20:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0011_auto_20200624_1420'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='content',
        ),
        migrations.RemoveField(
            model_name='message',
            name='title',
        ),
        migrations.AddField(
            model_name='message',
            name='comment',
            field=models.TextField(default=1, max_length=1000),
            preserve_default=False,
        ),
    ]
