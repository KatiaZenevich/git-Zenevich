from django.shortcuts import render
from .models import Ministry


def project_index(request):
    project = Ministry.objects.all()
    context = {
        'project': project
    }
    return render(request, 'project_index.html', context=context)