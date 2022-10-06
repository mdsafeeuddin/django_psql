# Generated by Django 4.1.1 on 2022-10-06 13:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('sql', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Query',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('query_text', models.CharField(max_length=200)),
                ('query_desc', models.CharField(max_length=200)),
                ('created', models.DateTimeField(verbose_name='date created')),
                ('updated', models.DateTimeField(verbose_name='date updated')),
                ('topic', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sql.topic')),
            ],
        ),
    ]
