# Generated by Django 2.1.7 on 2019-03-05 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('enrolment_number', models.CharField(blank=True, max_length=120, null=True)),
                ('user_type', models.CharField(choices=[('student', 'Student'), ('faculty', 'Faculty'), ('coordinator', 'Coordinator')], max_length=120)),
                ('semester', models.IntegerField()),
            ],
        ),
    ]
