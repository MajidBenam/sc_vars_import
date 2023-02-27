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

QING_VARS_FUNC = """
# THE temporary function for creating the my_sections_dic dic: test_for_varhier_dic inside utils
# and the qing_vars_links_creator() inside utils.py
def QingVars(request):
    my_sections_dic = {'Other_Sections': {'Other_Subsections': []},
 'Economy Variables': {'Productivity': [['Agricultural population',
    'agricultural_populations',
    'agricultural_population-create'],
   ['Arable land', 'arable_lands', 'arable_land-create'],
   ['Arable land per farmer',
    'arable_land_per_farmers',
    'arable_land_per_farmer-create'],
   ['Gross grain shared per agricultural population',
    'gross_grain_shared_per_agricultural_populations',
    'gross_grain_shared_per_agricultural_population-create'],
   ['Net grain shared per agricultural population',
    'net_grain_shared_per_agricultural_populations',
    'net_grain_shared_per_agricultural_population-create'],
   ['Surplus', 'surplus', 'surplus-create'],
   ['Gdp per capita', 'gdp_per_capitas', 'gdp_per_capita-create']],
  'State Finances': [['Military expense',
    'military_expenses',
    'military_expense-create'],
   ['Silver inflow', 'silver_inflows', 'silver_inflow-create'],
   ['Silver stock', 'silver_stocks', 'silver_stock-create']]},
 'Social Complexity Variables': {'Social Scale': [['Total population',
    'total_populations',
    'total_population-create']]},
 'Well Being': {'Biological Well-Being': [['Drought event',
    'drought_events',
    'drought_event-create'],
   ['Locust event', 'locust_events', 'locust_event-create'],
   ['Socioeconomic turmoil event',
    'socioeconomic_turmoil_events',
    'socioeconomic_turmoil_event-create'],
   ['Crop failure event', 'crop_failure_events', 'crop_failure_event-create'],
   ['Famine event', 'famine_events', 'famine_event-create'],
   ['Disease outbreak', 'disease_outbreaks', 'disease_outbreak-create']]}}
    # all_sections = Section.objects.all()
    # all_subsections = Subsection.objects.all()
    # all_varhiers = Variablehierarchy.objects.all()
    # meta_data_dict = {}
    # for ct in my_sections_dic.items():
    #     m = ct.model_class()
    #     #full_name = m.__module__ + m.__name__
    #     full_name = m.__name__
    #     meta_data_dict[full_name.lower()] = [full_name.split('.')[-1].replace("_", ' '), m._default_manager.count(), full_name.lower()+"-create",full_name.lower()+"s"]
    #     print (f".{m.__name__}	{m._default_manager.count()}")
    # my_dict = {}
    context = {}

    # for sect in all_sections:
    #     my_dict[sect] = {}
    #     for subsect in all_subsections:
    #         list_of_all_varhiers_in_here = []
    #         for item in all_varhiers:
    #             #print(item, item.section, item.subsection, sect.name, subsect.name)
    #             if item.section.name == sect.name and item.subsection.name == subsect.name:
    #                 print("We hit it")
    #                 list_of_all_varhiers_in_here.append(meta_data_dict[item.name.lower()])
    #         if list_of_all_varhiers_in_here:
    #             my_dict[sect][subsect] = list_of_all_varhiers_in_here
    context["my_dict"] = my_sections_dic
    return render(request, 'crisisdb/qing-vars.html', context=context)

"""

PLAYGROUND_FUNCS = """

def playground(request):
    if request.method == "POST":
        print(request.POST.get("selected_pols", 'Hallo'))
    all_pols = list_of_all_Polities()
    all_vars = dic_of_all_vars_with_varhier()
    all_vars_plus = dic_of_all_vars_in_sections()
    context = {'allpols': all_pols, 'all_var_hiers': all_vars, 'crisi': all_vars_plus}
    return render(request, 'crisisdb/playground.html', context=context)


Tags_dic = {
    'TRS': 'Evidenced',
    'DSP': 'Disputed',
    'SSP': 'Suspected',
    'IFR': 'Inferred',
    'UNK': 'Unknown',
}

def playgrounddownload(request):
    # read the data from the previous from
    # make sure you collect all the data from seshat_api
    # sort it out and spit it out
    # small task: download what we have on seshat_api
    checked_pols = request.POST.getlist("selected_pols")
    print("The checked politys are:", checked_pols)

    checked_vars = request.POST.getlist("selected_vars")
    print("The checked vars are:", checked_vars)

    new_checked_vars = ["crisisdb_" + item.lower() + '_related' for item in checked_vars]
    print("The modified checked vars are:", new_checked_vars)

    checked_separator = request.POST.get("SeparatorRadioOptions")
    print("The checked separator are:", checked_separator)

    if checked_separator == "comma":
        checked_sep = ","
    elif checked_separator == "bar":
        checked_sep = "|"
    else:
        print("Bad selection of Separator.")

    url = "http://127.0.0.1:8000/api/politys/"
    #url = "https://www.majidbenam.com/api/politys/"
    print(url)


    headers = CaseInsensitiveDict()
    headers["Accept"] = "application/json"

    resp = requests.get(url, headers=headers)

    all_my_data = resp.json()['results']

    final_response = HttpResponse(content_type='text/csv')
    now = datetime.datetime.now()
    now_str = now.strftime("%H%M%S")
    myfile_name = 'CrisisDB_data_' + str(request.user) + '_' + now_str
    final_response['Content-Disposition'] = f'attachment; filename="{myfile_name}.csv"'

    # print(all_my_data)
    writer = csv.writer(final_response, delimiter=checked_sep)
    # the top row is the same as Equinox, so no need to read data from user input for that
    writer.writerow(['polity', 'variable_name', 'variable_sub_name', 'value',
                     'year_from', 'year_to', 'certainty', 'references', 'notes'])

    for polity_with_everything in all_my_data:
        if polity_with_everything['name'] not in checked_pols:
            continue
        else:
            for variable in new_checked_vars:
                if variable not in polity_with_everything.keys():
                    continue
                else:
                    # we can get into a list of dictionaries
                    for var_instance in polity_with_everything[variable]:
                        all_inner_keys = var_instance.keys()
                        # print(all_inner_keys)
                        all_used_keys = []
                        for active_key in all_inner_keys:
                            if active_key not in ['year_from', 'year_to', 'tag'] and active_key not in all_used_keys:
                                an_equinox_row = []
                                an_equinox_row.append(
                                    polity_with_everything['name'])
                                an_equinox_row.append(
                                    variable[:-8])
                                an_equinox_row.append(
                                    active_key)
                                an_equinox_row.append(
                                    var_instance[active_key])
                                all_used_keys.append(active_key)
                                an_equinox_row.append(
                                    var_instance['year_from'])
                                an_equinox_row.append(
                                    var_instance['year_to'])
                                full_tag = Tags_dic[var_instance['tag']]
                                an_equinox_row.append(full_tag)
                                writer.writerow(an_equinox_row)

    return final_response

"""