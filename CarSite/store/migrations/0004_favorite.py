# Generated by Django 4.2.16 on 2024-10-18 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_rename_cars_history_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Favorite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('car', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.car')),
                ('cart', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='store.favoritecar')),
            ],
        ),
    ]