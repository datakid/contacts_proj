# Generated by Django 2.1.7 on 2019-02-27 02:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contacts', '0002_auto_20190227_1317'),
    ]

    operations = [
        migrations.CreateModel(
            name='Solutions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('notes', models.TextField(blank=True)),
                ('contact', models.ManyToManyField(to='contacts.Contact')),
            ],
        ),
    ]
