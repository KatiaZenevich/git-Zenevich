from django.urls import path
from .views import *

urlpatterns = [
    path('', project_index, name='project_index')

]
