# Generated by Django 4.0.4 on 2022-06-02 00:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('required_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Department',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Segment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='required_app.department')),
            ],
        ),
        migrations.CreateModel(
            name='SubSegment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('segment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='required_app.segment')),
            ],
        ),
        migrations.CreateModel(
            name='RequiredModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('required_id', models.IntegerField()),
                ('required_year', models.IntegerField()),
                ('required_date', models.DateField()),
                ('project_name', models.CharField(max_length=200)),
                ('consultant', models.CharField(blank=True, max_length=100, null=True)),
                ('owner', models.CharField(blank=True, max_length=100, null=True)),
                ('deadline', models.DateField(blank=True, null=True)),
                ('comments', models.CharField(blank=True, max_length=200, null=True)),
                ('ambere', models.CharField(blank=True, max_length=100, null=True)),
                ('client', models.ManyToManyField(to='required_app.client')),
                ('department', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='required_app.department')),
                ('sales_engineer', models.ManyToManyField(related_name='sales_engineer', to='required_app.engineer')),
                ('segment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='required_app.segment')),
                ('study_engineer', models.ManyToManyField(related_name='study_engineer', to='required_app.engineer')),
                ('sub_segment', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='required_app.subsegment')),
            ],
        ),
    ]