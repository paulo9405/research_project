from django.db import models


class SurveyResponse(models.Model):

    # Main question choices
    REASON_CHOICES = [
        ('learn_english',  'Learn English'),
        ('job',            'Job Opportunities'),
        ('quality_life',   'Quality of Life'),
        ('career',         'Career / Future'),
        ('other',          'Other'),
    ]

    # Main question
    reason       = models.CharField(max_length=20, choices=REASON_CHOICES)
    reason_other = models.TextField(blank=True)  # only filled when reason == 'other'

    # Personal information
    full_name    = models.CharField(max_length=100)
    age          = models.IntegerField()
    email        = models.EmailField()
    nationality  = models.CharField(max_length=100)
    city         = models.CharField(max_length=100)

    # Filled automatically on creation
    created_at   = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.full_name} — {self.get_reason_display()}"
