# Generated by Django 2.2 on 2021-06-08 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_userfeedback_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userfeedback',
            name='feedback',
            field=models.CharField(max_length=800),
        ),
        migrations.AlterField(
            model_name='userfeedback',
            name='name',
            field=models.CharField(max_length=70),
        ),
    ]
