# Generated by Django 3.0.5 on 2020-04-16 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_person'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='dob',
            field=models.DateField(auto_created=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
