# Generated by Django 4.2.4 on 2023-10-21 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user_app', '0002_user_interests'),
    ]

    operations = [
        migrations.CreateModel(
            name='Portal',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flowchart', models.TextField(blank=True, null=True)),
                ('tfi_score', models.IntegerField(blank=True, null=True)),
                ('next_step', models.CharField(blank=True, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user_app.user')),
            ],
        ),
    ]
