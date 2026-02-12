from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import SurveyResponse


def survey_form(request):
    """Screen 1 — Main survey form at /"""

    if request.method == 'POST':
        # Save form data to the database
        SurveyResponse.objects.create(
            reason       = request.POST.get('reason'),
            reason_other = request.POST.get('reason_other', ''),
            full_name    = request.POST.get('full_name'),
            age          = request.POST.get('age'),
            email        = request.POST.get('email'),
            nationality  = request.POST.get('nationality'),
            city         = request.POST.get('city'),
        )
        return redirect('thanks')  # redirect to /thanks/

    return render(request, 'survey/survey_form.html')


def thanks(request):
    """Screen 2 — Thank you page at /thanks/"""
    return render(request, 'survey/thanks.html')


@login_required
def results(request):
    """Screen 3 — Results dashboard at /results/ (login required)"""

    total = SurveyResponse.objects.count()

    # Count per reason — used as Chart.js data
    reasons = {}
    for key, label in SurveyResponse.REASON_CHOICES:
        reasons[label] = SurveyResponse.objects.filter(reason=key).count()

    # Count per age group
    age_groups = {
        '18-24': SurveyResponse.objects.filter(age__gte=18, age__lte=24).count(),
        '25-34': SurveyResponse.objects.filter(age__gte=25, age__lte=34).count(),
        '35+':   SurveyResponse.objects.filter(age__gte=35).count(),
    }

    context = {
        'total':      total,
        'reasons':    reasons,
        'age_groups': age_groups,
    }
    return render(request, 'survey/results.html', context)
