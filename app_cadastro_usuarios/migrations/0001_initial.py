# Generated by Django 4.1.7 on 2023-03-21 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id_usuario', models.AutoField(primary_key=True, serialize=False)),
                ('Nome', models.TextField(max_length=255)),
                ('Idade', models.IntegerField()),
            ],
        ),
    ]
