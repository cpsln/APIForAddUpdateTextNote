# Generated by Django 3.0.3 on 2020-03-04 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='UrbanstopNotetext',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('CreationDate', models.DateTimeField(auto_created=True, auto_now_add=True)),
                ('UserName', models.CharField(max_length=40)),
                ('TextNote', models.CharField(max_length=1000)),
                ('UpdateDate', models.DateTimeField(blank=True, null=True)),
                ('LastUpdateDate', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
