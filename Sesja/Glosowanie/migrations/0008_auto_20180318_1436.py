# Generated by Django 2.0.3 on 2018-03-18 13:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Glosowanie', '0007_auto_20180318_1423'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='uchwala',
            options={'verbose_name': 'Uchwała', 'verbose_name_plural': 'Uchwały'},
        ),
        migrations.AlterField(
            model_name='glosowanie',
            name='id_uzytkownika',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]