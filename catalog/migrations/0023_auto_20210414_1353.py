# Generated by Django 3.1.1 on 2021-04-14 20:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0022_merge_20180115_2033'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name', 'first_name']},
        ),
    ]
