# Generated by Django 4.2.6 on 2023-10-12 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_app', '0002_legume_delete_prof'),
    ]

    operations = [
        migrations.CreateModel(
            name='Fermier',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('prenom', models.CharField(max_length=50)),
                ('nom', models.CharField(max_length=50)),
            ],
        ),
    ]