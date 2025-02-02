# Generated by Django 2.2.5 on 2019-09-10 15:11

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Budget',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('year', models.IntegerField(choices=[(1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020)], default=2019, verbose_name='year')),
                ('quarter', models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4)], verbose_name='quarter')),
                ('type', models.CharField(choices=[('Before Quarter', 'Before Quarter'), ('During Quarter', 'During Quarter')], max_length=30, verbose_name='type')),
                ('product', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='WBS_Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cc_index', models.CharField(max_length=20)),
                ('name', models.CharField(max_length=200)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('budget', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.Budget')),
            ],
        ),
        migrations.CreateModel(
            name='Transfer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.IntegerField()),
                ('timeInitiated', models.DateTimeField(default=datetime.datetime(2019, 9, 10, 15, 11, 29, 536655))),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('status', models.BooleanField(default=True)),
                ('transfer_target', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='transfer_target', to='dashboard.WBS_Item')),
                ('wbs_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='wbs_item', to='dashboard.WBS_Item')),
            ],
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(default=datetime.datetime(2019, 9, 10, 15, 11, 29, 537095))),
                ('text', models.CharField(blank=True, max_length=3000)),
                ('attachment', models.FileField(blank=True, upload_to='photos/%Y/%m/%d/')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wbs_item', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dashboard.WBS_Item')),
            ],
        ),
    ]
