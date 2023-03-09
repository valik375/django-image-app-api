# Generated by Django 4.1.7 on 2023-03-09 08:34

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(default=None, null=True, upload_to='images')),
                ('link_lifetime_created', models.DateTimeField(blank=True, null=True)),
                ('link_lifetime_in_seconds', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(300), django.core.validators.MaxValueValidator(30000)])),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='image', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
