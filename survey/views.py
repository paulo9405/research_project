import json
from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import SurveyResponse


def survey_form(request):
    """Screen 1 — Main survey form at /"""

    if request.method == 'POST':
        SurveyResponse.objects.create(
            reason            = request.POST.get('reason', ''),
            reason_other      = request.POST.get('reason_other', ''),
            time_in_ireland   = request.POST.get('time_in_ireland', ''),
            status_in_ireland = request.POST.get('status_in_ireland', ''),
            employed          = request.POST.get('employed', ''),
            cost_of_living    = request.POST.get('cost_of_living', ''),
            plan_to_stay      = request.POST.get('plan_to_stay', ''),
            full_name         = request.POST.get('full_name'),
            age               = request.POST.get('age'),
            email             = request.POST.get('email'),
            nationality       = request.POST.get('nationality'),
            city              = request.POST.get('city'),
        )
        return redirect('results')  # go straight to results

    return render(request, 'survey/survey_form.html')


def thanks(request):
    """Thank you page (kept for compatibility)"""
    return render(request, 'survey/thanks.html')


def results(request):
    """Results dashboard at /results/"""
    return render(request, 'survey/results.html')


def results_data(request):
    """JSON API — live data for the results dashboard"""

    total = SurveyResponse.objects.count()

    reasons = {}
    for key, label in SurveyResponse.REASON_CHOICES:
        count = SurveyResponse.objects.filter(reason=key).count()
        if count:
            reasons[label] = count

    age_groups = {
        '18–24': SurveyResponse.objects.filter(age__gte=18, age__lte=24).count(),
        '25–34': SurveyResponse.objects.filter(age__gte=25, age__lte=34).count(),
        '35+':   SurveyResponse.objects.filter(age__gte=35).count(),
    }

    time_labels = {}
    for key, label in SurveyResponse.TIME_IN_IRELAND_CHOICES:
        count = SurveyResponse.objects.filter(time_in_ireland=key).count()
        if count:
            time_labels[label] = count

    status_data = {}
    for key, label in SurveyResponse.STATUS_CHOICES:
        count = SurveyResponse.objects.filter(status_in_ireland=key).count()
        if count:
            status_data[label] = count

    cost_data = {}
    for key, label in SurveyResponse.COST_OF_LIVING_CHOICES:
        count = SurveyResponse.objects.filter(cost_of_living=key).count()
        if count:
            cost_data[label] = count

    stay_data = {}
    for key, label in SurveyResponse.PLAN_TO_STAY_CHOICES:
        count = SurveyResponse.objects.filter(plan_to_stay=key).count()
        if count:
            stay_data[label] = count

    employed_yes = SurveyResponse.objects.filter(employed='yes').count()
    employed_no  = SurveyResponse.objects.filter(employed='no').count()

    return JsonResponse({
        'total':       total,
        'reasons':     reasons,
        'age_groups':  age_groups,
        'time':        time_labels,
        'status':      status_data,
        'employed':    {'Employed': employed_yes, 'Not Employed': employed_no},
        'cost':        cost_data,
        'stay':        stay_data,
    })
