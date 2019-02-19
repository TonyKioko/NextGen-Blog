# Generated by Django 2.1.5 on 2019-02-19 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('Science', 'Science'), ('Technology', 'Technology'), ('Travel', 'Travel'), ('Food', 'Food'), ('Lifestyle', 'Lifestyle'), ('Fashion', 'Fashion')], default='Science', max_length=80),
        ),
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(upload_to='blog_pics/'),
        ),
    ]
