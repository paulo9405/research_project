from django.db import models


class SurveyResponse(models.Model):

    REASON_CHOICES = [
        ('learn_english', 'Learn English'),
        ('job',           'Job Opportunities'),
        ('quality_life',  'Quality of Life'),
        ('career',        'Career / Future'),
        ('other',         'Other'),
    ]

    TIME_IN_IRELAND_CHOICES = [
        ('less_6m', 'Less than 6 months'),
        ('6_12m',   '6–12 months'),
        ('1_3y',    '1–3 years'),
        ('3y_plus', '3+ years'),
    ]

    STATUS_CHOICES = [
        ('student', 'Student'),
        ('worker',  'Worker'),
        ('both',    'Both'),
        ('other',   'Other'),
    ]

    EMPLOYED_CHOICES = [
        ('yes', 'Yes'),
        ('no',  'No'),
    ]

    COST_OF_LIVING_CHOICES = [
        ('yes',     'Yes'),
        ('no',      'No'),
        ('neutral', 'Neutral'),
    ]

    PLAN_TO_STAY_CHOICES = [
        ('yes',      'Yes'),
        ('no',       'No'),
        ('not_sure', 'Not sure'),
    ]

    # Main question
    reason            = models.CharField(max_length=20, choices=REASON_CHOICES)
    reason_other      = models.TextField(blank=True)

    # New questions
    time_in_ireland   = models.CharField(max_length=20, choices=TIME_IN_IRELAND_CHOICES, blank=True)
    status_in_ireland = models.CharField(max_length=20, choices=STATUS_CHOICES, blank=True)
    employed          = models.CharField(max_length=10, choices=EMPLOYED_CHOICES, blank=True)
    cost_of_living    = models.CharField(max_length=10, choices=COST_OF_LIVING_CHOICES, blank=True)
    plan_to_stay      = models.CharField(max_length=10, choices=PLAN_TO_STAY_CHOICES, blank=True)

    # Personal information
    full_name         = models.CharField(max_length=100)
    age               = models.IntegerField()
    email             = models.EmailField()
    nationality       = models.CharField(max_length=100)
    city              = models.CharField(max_length=100)

    created_at        = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} — {self.get_reason_display()}"
