# Generated by Django 4.2.5 on 2023-09-17 19:50

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usac', '0003_alter_customuser_code_alter_customuser_email_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='customuser',
            old_name='code',
            new_name='food_code',
        ),
    ]
