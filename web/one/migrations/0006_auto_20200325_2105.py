# Generated by Django 3.0.2 on 2020-03-25 15:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('one', '0005_interview_package'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoryposts',
            old_name='desc',
            new_name='interview_procedure',
        ),
    ]
