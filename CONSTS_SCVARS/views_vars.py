# We most probably don't need the old vars_dic that we copy/pasted in views.py as it was used in the old QingVars function
VIEWS_IMPORTS = """
from seshat.utils.utils import adder, dic_of_all_vars, list_of_all_Polities, dic_of_all_vars_in_sections, dic_of_all_vars_with_varhier
from django.db.models.base import Model
# from django.http.response import HttpResponse
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.contrib.auth.decorators import login_required, permission_required
from django.utils.safestring import mark_safe
from django.views.generic.list import ListView

from django.contrib.contenttypes.models import ContentType

from django.views.generic.edit import CreateView, UpdateView, DeleteView

from django.http import HttpResponseRedirect, response, JsonResponse
from ..core.models import Citation, Reference, Polity, Section, Subsection, Country, Variablehierarchy

# from .mycodes import *
from django.conf import settings

from django.urls import reverse, reverse_lazy

from django.views import generic
import csv
import datetime

from django.core.paginator import Paginator

from django.http import HttpResponse

import requests
from requests.structures import CaseInsensitiveDict

"""

