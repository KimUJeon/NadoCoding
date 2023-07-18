from django.shortcuts import render
from . import models


def list_patients(request):
    all_patients = models.Patient.objects.all()
    context = {"patients": all_patients}

    return render(request, "my_app/list.html", context=context)


def example_view(request):
    return render(request, 'my_app/example.html')

def variable_view(request):
    return render(request, 'my_app/variable.html')