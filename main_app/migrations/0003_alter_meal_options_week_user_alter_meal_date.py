# Generated by Django 4.2.11 on 2024-05-01 20:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('main_app', '0002_meal'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='meal',
            options={'ordering': ('-date',)},
        ),
        migrations.AddField(
            model_name='week',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='meal',
            name='date',
            field=models.DateField(verbose_name='meal date'),
        ),
    ]
