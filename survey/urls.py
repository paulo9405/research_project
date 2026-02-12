from django.urls import path
from . import views

urlpatterns = [
    path('',         views.survey_form, name='survey_form'),
    path('thanks/',  views.thanks,      name='thanks'),
    path('results/', views.results,     name='results'),
]
