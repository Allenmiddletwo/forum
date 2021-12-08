# Generated by Django 3.2.7 on 2021-12-08 03:30

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=255, verbose_name='討論主題')),
                ('content', models.TextField(verbose_name='內文')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='建立時間')),
                ('replied', models.DateTimeField(blank=True, null=True, verbose_name='回覆時間')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
