# Generated by Django 3.1.5 on 2021-01-26 07:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Candidate',
            fields=[
                ('firstName', models.CharField(max_length=64)),
                ('middleName', models.CharField(max_length=64)),
                ('lastName', models.CharField(max_length=64)),
                ('emailId', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('gender', models.CharField(choices=[('M', 'Male'), ('F', 'Female')], max_length=1)),
                ('universityRollNo', models.CharField(max_length=64)),
                ('graduationCGPA', models.FloatField(null=True)),
                ('graduationYear', models.IntegerField(null=True)),
                ('collegeName', models.CharField(max_length=254)),
                ('experience', models.IntegerField(null=True)),
                ('mobileNo', models.CharField(max_length=10)),
                ('DOB', models.DateField(auto_now=True)),
                ('projectsLink', models.URLField(null=True)),
                ('resume', models.FileField(upload_to=None)),
                ('noticePeriod', models.IntegerField(null=True)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('name', models.CharField(max_length=64)),
                ('emailId', models.EmailField(max_length=254, null=True)),
                ('incedoCode', models.CharField(default='123', max_length=64, primary_key=True, serialize=False)),
                ('password', models.CharField(max_length=64)),
                ('tempPassword', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('requisitionId', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=100)),
                ('timestamp', models.DateTimeField()),
                ('positionOwner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Incedoinc.employee')),
            ],
        ),
        migrations.CreateModel(
            name='Feedback',
            fields=[
                ('feedbackId', models.AutoField(primary_key=True, serialize=False)),
                ('level', models.IntegerField(null=True)),
                ('status', models.CharField(choices=[('P', 'pass'), ('F', 'fail')], max_length=1)),
                ('ratingPython', models.IntegerField(null=True)),
                ('ratingJava', models.IntegerField(null=True)),
                ('ratingCPP', models.IntegerField(null=True)),
                ('ratingSQL', models.IntegerField(null=True)),
                ('comments', models.TextField(max_length=500)),
                ('timestamp', models.DateTimeField()),
                ('candidateEmail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Incedoinc.candidate')),
                ('interviewerCode', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Incedoinc.employee')),
            ],
        ),
        migrations.CreateModel(
            name='CandidateJobInfo',
            fields=[
                ('jobInfoId', models.AutoField(primary_key=True, serialize=False)),
                ('emailId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Incedoinc.candidate')),
                ('requisitionId', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Incedoinc.job')),
            ],
        ),
        migrations.AddField(
            model_name='candidate',
            name='registeredBy',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Incedoinc.employee'),
        ),
    ]
