# Generated by Django 2.0.7 on 2018-07-24 10:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('artist', models.CharField(default='', max_length=200)),
                ('title', models.CharField(max_length=256)),
                ('thumbnail', models.FileField(upload_to='media')),
                ('video', models.CharField(default='', max_length=512)),
                ('uploadAt', models.DateTimeField(blank=True, null=True)),
            ],
        ),
    ]
