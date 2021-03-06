# Generated by Django 2.2.4 on 2019-10-01 13:24
# ... and manually updated :)

from django.db import migrations, models


def copy_scores(apps, schema_editor):
    # noinspection PyPep8Naming
    Review = apps.get_model('review', 'Review')
    reviews = Review.objects.all()
    for review in reviews:
        if review.clarity:
            review.int_clarity = int(review.clarity)
        if review.originality:
            review.int_originality = int(review.originality)
        if review.relevance:
            review.int_relevance = int(review.relevance)
        if review.technical_merit:
            review.int_technical_merit = int(review.technical_merit)
    Review.objects.bulk_update(
        reviews, ['int_clarity', 'int_originality', 'int_relevance',
                  'int_technical_merit'])


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0007_rewire_reviews_to_stage'),
    ]

    operations = [
        migrations.AddField(
            model_name='review',
            name='int_clarity',
            field=models.IntegerField(blank=True, choices=[(None, 'Choose your score'), (1, '1 - Very Poor'), (2, '2 - Below Average'), (3, '3 - Average'), (4, '4 - Good'), (5, '5 - Excellent')], default=None, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='int_originality',
            field=models.IntegerField(blank=True, choices=[(None, 'Choose your score'), (1, '1 - Very Poor'), (2, '2 - Below Average'), (3, '3 - Average'), (4, '4 - Good'), (5, '5 - Excellent')], default=None, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='int_relevance',
            field=models.IntegerField(blank=True, choices=[(None, 'Choose your score'), (1, '1 - Very Poor'), (2, '2 - Below Average'), (3, '3 - Average'), (4, '4 - Good'), (5, '5 - Excellent')], default=None, null=True),
        ),
        migrations.AddField(
            model_name='review',
            name='int_technical_merit',
            field=models.IntegerField(blank=True, choices=[(None, 'Choose your score'), (1, '1 - Very Poor'), (2, '2 - Below Average'), (3, '3 - Average'), (4, '4 - Good'), (5, '5 - Excellent')], default=None, null=True),
        ),
        migrations.RunPython(copy_scores),

        migrations.RemoveField(model_name='review', name='clarity'),
        migrations.RemoveField(model_name='review', name='originality'),
        migrations.RemoveField(model_name='review', name='relevance'),
        migrations.RemoveField(model_name='review', name='technical_merit'),

        migrations.RenameField(
            model_name='review',
            old_name='int_clarity', new_name='clarity'),
        migrations.RenameField(
            model_name='review',
            old_name='int_originality', new_name='originality'),
        migrations.RenameField(
            model_name='review',
            old_name='int_relevance', new_name='relevance'),
        migrations.RenameField(
            model_name='review',
            old_name='int_technical_merit', new_name='technical_merit'),
    ]
