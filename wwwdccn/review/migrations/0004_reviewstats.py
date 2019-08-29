# Generated by Django 2.2.4 on 2019-08-28 14:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conferences', '0010_proceedingvolume'),
        ('review', '0003_decision'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewStats',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_submissions_reviewed', models.IntegerField(default=0, verbose_name='Number of submissions with all reviews submitted')),
                ('num_submissions_with_incomplete_reviews', models.IntegerField(default=0, verbose_name='Number of submissions with incomplete reviews')),
                ('num_submissions_with_missing_reviewers', models.IntegerField(default=0, verbose_name='Number of submissions missing one or more reviewers')),
                ('average_score', models.FloatField(default=0.0, verbose_name='Average score over all completely reviewed submissions')),
                ('median_score', models.FloatField(default=0.0, verbose_name='Median score over all completely reviewed submissions')),
                ('q1_score', models.FloatField(default=0.0, verbose_name='Q1 score (25% are not greater then)')),
                ('q3_score', models.FloatField(default=0.0, verbose_name='Q3 score (25% are not less then)')),
                ('conference', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='review_stats', to='conferences.Conference')),
            ],
        ),
    ]
