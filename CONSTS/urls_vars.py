URL_BASE_IMPORTS = """
from django.urls import path

from . import views

urlpatterns = [
    path('vars/', views.QingVars, name='qing_vars'),
    path('playground/', views.playground, name='playground'),
    path('playgrounddownload/', views.playgrounddownload,
         name="playgrounddownload"), 
]

"""