# Generated by Django 4.0.8 on 2022-12-18 17:12

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('home', '0001_initial'),
        ('blogs', '0001_initial'),
        ('wagtailpod', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='homepagefeaturedpodcast',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='wagtailpod.podcastpage'),
        ),
        migrations.AddField(
            model_name='homepagefeaturedpodcast',
            name='home_page',
            field=modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='featured_podcasts', to='home.homepage'),
        ),
        migrations.AddField(
            model_name='homepagefeaturedblog',
            name='event',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to='blogs.blog'),
        ),
        migrations.AddField(
            model_name='homepagefeaturedblog',
            name='home_page',
            field=modelcluster.fields.ParentalKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='featured_blogs', to='home.homepage'),
        ),
    ]
