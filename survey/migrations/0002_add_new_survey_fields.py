from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='surveyresponse',
            name='time_in_ireland',
            field=models.CharField(
                blank=True,
                choices=[
                    ('less_6m', 'Less than 6 months'),
                    ('6_12m',   '6\u201312 months'),
                    ('1_3y',    '1\u20133 years'),
                    ('3y_plus', '3+ years'),
                ],
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name='surveyresponse',
            name='status_in_ireland',
            field=models.CharField(
                blank=True,
                choices=[
                    ('student', 'Student'),
                    ('worker',  'Worker'),
                    ('both',    'Both'),
                    ('other',   'Other'),
                ],
                max_length=20,
            ),
        ),
        migrations.AddField(
            model_name='surveyresponse',
            name='employed',
            field=models.CharField(
                blank=True,
                choices=[('yes', 'Yes'), ('no', 'No')],
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name='surveyresponse',
            name='cost_of_living',
            field=models.CharField(
                blank=True,
                choices=[('yes', 'Yes'), ('no', 'No'), ('neutral', 'Neutral')],
                max_length=10,
            ),
        ),
        migrations.AddField(
            model_name='surveyresponse',
            name='plan_to_stay',
            field=models.CharField(
                blank=True,
                choices=[('yes', 'Yes'), ('no', 'No'), ('not_sure', 'Not sure')],
                max_length=10,
            ),
        ),
    ]
