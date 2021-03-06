# Generated by Django 3.2.9 on 2021-11-20 07:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20211119_2116'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='category',
            field=models.CharField(choices=[('html', 'Html'), ('css', 'Css'), ('javascript', 'Javascript'), ('python', 'Python')], default='Python', max_length=128),
        ),
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
