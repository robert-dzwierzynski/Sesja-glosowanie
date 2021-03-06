# Generated by Django 2.0.3 on 2018-03-18 10:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Uchwala',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Tytuł uchwały')),
                ('body', models.TextField(verbose_name='Treść uchwały')),
                ('is_visible', models.BooleanField(verbose_name='Widoczna')),
            ],
        ),
    ]
