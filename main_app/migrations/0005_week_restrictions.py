# Generated by Django 4.2.11 on 2024-05-02 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_restriction'),
    ]

    operations = [
        migrations.AddField(
            model_name='week',
            name='restrictions',
            field=models.ManyToManyField(to='main_app.restriction'),
        ),
    ]
