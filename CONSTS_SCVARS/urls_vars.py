URL_BASE_IMPORTS = """
from django.urls import path

from . import views

urlpatterns = [
    path('scvars/', views.scvars, name='scvars'),
]

"""