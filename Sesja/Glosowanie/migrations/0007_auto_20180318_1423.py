# Generated by Django 2.0.3 on 2018-03-18 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Glosowanie', '0006_auto_20180318_1355'),
    ]

    operations = [
        migrations.AlterField(
            model_name='glosowanie',
            name='vote',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Za'), (0, 'Przeciw'), (2, 'Wstrzymuję się')]),
        ),
    ]
