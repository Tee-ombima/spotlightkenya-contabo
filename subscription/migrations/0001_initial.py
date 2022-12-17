# Generated by Django 4.0.8 on 2022-12-17 19:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailcore', '0078_referenceindex'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManageSubscriptionPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='SubscriptionIndexPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('intro', wagtail.fields.RichTextField(blank=True)),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('format', models.CharField(choices=[('pdf', 'PDF'), ('print', 'Print'), ('print_and_pdf', 'Print and PDF')], default='pdf', max_length=255)),
                ('price_group', models.CharField(choices=[('normal', 'Normal'), ('true_cost', 'True cost'), ('low_income', 'Low income'), ('international', 'International')], default='normal', max_length=255)),
                ('price', models.IntegerField(editable=False)),
                ('recurring', models.BooleanField(default=True)),
                ('start_date', models.DateField(null=True)),
                ('end_date', models.DateField(null=True)),
                ('subscriber_given_name', models.CharField(default='', help_text='Enter the given (first) name for the subscriber.', max_length=255)),
                ('subscriber_family_name', models.CharField(default='', help_text='Enter the family (last) name for the subscriber.', max_length=255)),
                ('subscriber_organization', models.CharField(blank=True, max_length=255, null=True)),
                ('subscriber_street_address', models.CharField(blank=True, default='', help_text='The street address where a print subscription could be mailed', max_length=255)),
                ('subscriber_street_address_line_2', models.CharField(blank=True, default='', help_text='If needed, second line for mailing address', max_length=255)),
                ('subscriber_postal_code', models.CharField(blank=True, help_text='Postal code for the mailing address', max_length=16)),
                ('subscriber_address_locality', models.CharField(blank=True, help_text='City for the mailing address', max_length=255)),
                ('subscriber_address_region', models.CharField(blank=True, default='', help_text='State for the mailing address', max_length=255)),
                ('subscriber_address_country', models.CharField(blank=True, default='United States', help_text='Country for mailing', max_length=255)),
                ('paid', models.BooleanField(default=False)),
                ('braintree_subscription_id', models.CharField(blank=True, help_text='DO NOT EDIT. Used to cross-reference subscriptions with Braintree payments.', max_length=255)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='subscriptions', to=settings.AUTH_USER_MODEL, verbose_name='subscriber email')),
            ],
        ),
    ]
