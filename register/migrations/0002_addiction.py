# Generated by Django 3.1.5 on 2021-01-21 23:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Addiction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_addiction', models.CharField(max_length=200)),
                ('type_addiction', models.CharField(max_length=200)),
                ('homeless', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='register.homeless')),
            ],
            options={
                'db_table': 'addiction',
            },
        ),
    ]
