# Generated by Django 3.2.25 on 2024-03-23 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='LoginTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('password', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Usertable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.BigIntegerField(max_length=12)),
                ('email', models.CharField(max_length=50)),
                ('address', models.CharField(max_length=60)),
                ('photo', models.FileField(upload_to='')),
                ('LOGIN', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sentimentapp.logintable')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('feedback', models.CharField(max_length=800)),
                ('date', models.DateField()),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sentimentapp.usertable')),
            ],
        ),
        migrations.CreateModel(
            name='Complaint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('complaint', models.CharField(max_length=800)),
                ('replydate', models.DateField()),
                ('USER', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sentimentapp.usertable')),
            ],
        ),
    ]
