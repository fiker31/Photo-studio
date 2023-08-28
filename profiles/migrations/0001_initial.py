# Generated by Django 2.2.5 on 2020-07-14 13:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('posts', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('propic', models.ImageField(null=True, upload_to='')),
                ('bio', models.CharField(blank=True, max_length=224, null=True)),
                ('P_number', models.CharField(blank=True, max_length=64, null=True)),
                ('telegram', models.CharField(blank=True, max_length=50, null=True)),
                ('instagram', models.CharField(blank=True, max_length=50, null=True)),
                ('like', models.ManyToManyField(to='posts.Images')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
