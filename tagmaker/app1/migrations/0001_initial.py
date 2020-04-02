# Generated by Django 3.0.5 on 2020-04-02 06:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Document',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(blank=True, max_length=255)),
                ('photo', models.ImageField(default='defo', upload_to='documents/')),
                ('uploaded_at', models.DateTimeField(auto_now_add=True)),
                ('output', models.ImageField(default='output/output.jpg', upload_to='')),
            ],
        ),
    ]
