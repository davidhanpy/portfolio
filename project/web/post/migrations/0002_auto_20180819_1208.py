# Generated by Django 2.1 on 2018-08-19 12:08

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('post', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PostScore',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('score', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.FileField(default='', upload_to='media'),
        ),
        migrations.AddField(
            model_name='postscore',
            name='post',
            field=models.ForeignKey(on_delete='CASCADE', to='post.Post'),
        ),
        migrations.AddField(
            model_name='postscore',
            name='user',
            field=models.ForeignKey(on_delete='CASCADE', to=settings.AUTH_USER_MODEL),
        ),
    ]
