# old comma_value_maker
def human_readable_varname_from_dic(v):
    # input must be a dictionary
    if "varname" not in v.keys() or "dtype" not in v.keys():
        print("Invalid dictionary as input")
        return 0
    elif v["dtype"][0] in ["IntegerField", "PositiveBigIntegerField",]:
        return v["varname"] + "|intcomma"
    else:
        return v["varname"]

def importance_maker(v):
    if "importance" in v.keys():
        return v["importance"]
    else:
        return "NORMAL"

def underscore_to_space(mystr):
    spaced_value_list_0 = mystr.split("_")
    spaced_value_list = []
    for item in spaced_value_list_0:
        if len(item) >= 3 and item.lower() not in ["for", "and", "from", "the"]:
            spaced_value_list.append(item.capitalize())
        else:
            spaced_value_list.append(item)

    spaced_value = " ".join([myvalue for myvalue in spaced_value_list])
    return spaced_value
              
def col_heading_maker(k, col_name, heading, note, importance):
    # importance must be chosen carefully
    if importance == "HIGH":
        font_class = "fw-bold"
    elif importance == "LOW":
        font_class = "fw-light"
    else:
        font_class = "fw-normal"

    # make all heading fonts bold:
    font_class= "fw-bold"
    # note can be done carefully as well
    return f'''<th class = "{font_class}" style="text-align: center;" scope="col"><span>
    <a href="{{% url '{k}s_all' %}}?orderby={col_name}&orderby2=tag"><i class="fa-solid fa-caret-down"></i></a>
</span>{heading}
</th>'''

def inner_value_maker_list(actual_value, importance):
    """
    This will be used for the values that go inside the lists
    """
    # importance must be chosen carefully
    if importance == "HIGH":
        font_class = "fw-bold"
    elif importance == "LOW":
        font_class = "fw-light"
    else:
        font_class = "fw-normal"
                
    return f'''
<td class = "{{% if obj.tag == 'DSP' %}}
text-danger
{{% elif obj.tag == 'SSP' %}}
text-warning
{{% elif obj.tag == 'UNK' %}}
text-secondary
{{% elif obj.tag == 'IFR' %}}
text-primary
{{% else %}}
text-success
{{% endif %}} {font_class}" style="text-align: center;">
<h6 class="pt-3">{{{{ obj.{actual_value} }}}}</h6>
</td>'''
              
def inner_value_maker_detail(actual_value, importance):
    """
    This will be used for the values that go inside the lists
    """
    # importance must be chosen carefully
    if importance == "HIGH":
        font_class = "fw-bold"
    elif importance == "LOW":
        font_class = "fw-light"
    else:
        font_class = "fw-normal"
                
    return f'''
<td class = "{{% if object.tag == 'DSP' %}}
text-danger
{{% elif object.tag == 'SSP' %}}
text-warning
{{% elif object.tag == 'UNK' %}}
text-secondary
{{% elif object.tag == 'IFR' %}}
text-primary
{{% else %}}
text-success
{{% endif %}} {font_class}" style="text-align: center;">
<h6>{{{{ object.{actual_value} }}}}</h6>
<p> <small>{{% if object.tag == "DSP" %}}
    <span class="badge rounded-pill bg-danger">{{{{ object.get_tag_display }}}}</span>
    {{% elif  object.tag == "SSP" %}}
     <span class="badge rounded-pill bg-warning text-dark">{{{{ object.get_tag_display }}}}</span>
    {{% elif  object.tag == "UNK" %}}
    <span class="badge rounded-pill bg-secondary">{{{{ object.get_tag_display }}}}</span>
    {{% elif  object.tag == "IFR" %}}
    <span class="badge rounded-pill bg-primary">{{{{ object.get_tag_display }}}}</span>
    {{% else  %}}
    <span class="badge rounded-pill bg-success">{{{{ object.get_tag_display }}}}</span>
    {{% endif %}}</small></p>
</td>'''
          

def main_description_maker(v):
    """
    This will be used for the descriptions to be shown on top of the pages.
    """
    if 'maindesc' in v.keys():
        main_descr = str(v['maindesc'])
        return f'''
<div class="row">
<p>
{main_descr}
</p>
</div>
'''
    else:
        return ""
    
def string_pluralizer_capitalizer(k):
    plural_form = k + 's'
    if k[-1] == "y":
        plural_form = k[:-1].capitalize() + "ies"
    if k[-1] == "x" or k[-1] == "z":
        plural_form = k.capitalize() + "es"
    if k[-1] == "s":
        plural_form = k.capitalize()
    return plural_form

def string_pluralizer(k):
    plural_form = k + 's'
    if k[-1] == "y":
        plural_form = k[:-1] + "ies"
    if k[-1] == "x" or k[-1] == "z":
        plural_form = k + "es"
    if k[-1] == "s":
        plural_form = k
    return plural_form

def has_any_uppercase(s):
    return any(ele.isupper() for ele in s)

def width_decider(form_variable, num_of_columns):
    if num_of_columns in [1,2,3]:
        div = 6
    elif num_of_columns == 4:
        div = 4
    elif num_of_columns == 5:
        div = 3
    else:
        div = 4

    # return 3 for everything
    div = 3
    return f'''
<div class="col-md-{div} mb-2">
{{{{ form.{form_variable}|as_crispy_field }}}}
</div>'''


def show_values_general(is_choice, my_meaty_varnames):
    if len(my_meaty_varnames) == 2 and "year_from" in my_meaty_varnames[0] and "year_to" in my_meaty_varnames[1]:
        _from = my_meaty_varnames[0]
        _to = my_meaty_varnames[1]
        return f"""
    def show_value(self):
        if self.{_from} == self.{_to}:
            if self.{_from} < 0:
                return f'{{abs(self.{_from}):,}}' + " BCE" 
            else:
                return f'{{abs(self.{_from}):,}}' + " CE" 
        elif self.{_to} == None:
            if self.{_from} < 0:
                return f'{{abs(self.{_from}):,}}' + " BCE" 
            else:
                return f'{{abs(self.{_from}):,}}' + " CE" 
        elif self.{_to} == None and  self.{_from} == None:
            return " - " 
        else:
            if self.{_from} < 0 and self.{_to} < 0:
                return "[" + f'{{abs(self.{_from}):,}}' + " BCE"  + " \u279c " + f'{{abs(self.{_to}):,}}' + " BCE"  + "]"
            elif  self.{_from} < 0 and self.{_to} >= 0:
                return "[" + f'{{abs(self.{_from}):,}}' + " BCE"  + " \u279c " + f'{{abs(self.{_to}):,}}' + " CE"  + "]"
            else:
                return "[" + f'{{abs(self.{_from}):,}}' + " CE"  + " \u279c " + f'{{abs(self.{_to}):,}}' + " CE" + "]"
        """
    elif len(my_meaty_varnames) == 2 and "_from" in my_meaty_varnames[0] and "_to" in my_meaty_varnames[1]:
        _from = my_meaty_varnames[0]
        _to = my_meaty_varnames[1]
        return f"""
    def show_value(self):
        if self.{_from} and self.{_to} and self.{_to} == self.{_from}:
            return self.{_from}
        elif self.{_from} and self.{_to}:
            return f"[{{self.{_from}:,}} to {{self.{_to}:,}}]"
        elif self.{_from}:
            return f"[{{self.{_from}:,}}"
        elif self.{_to}:
            return f"[{{self.{_to}:,}}"
        else:
            return " - "
        """
    elif ((not is_choice) and len(my_meaty_varnames) == 1):
        value = my_meaty_varnames[0]
        return f"""
    def show_value(self):
        if self.{value}:
            return self.{value}
        else:
            return " - "
        """
    elif is_choice and len(my_meaty_varnames) == 1:
        value = my_meaty_varnames[0]
        return f"""
    def show_value(self):
        if self.{value}:
            return self.get_{value}_display()
        else:
            return " - "
        """
    else:
        print(f"BAd case...{my_meaty_varnames}")

def get_the_radios(col_name):
    return f"""
<div class="col-md-3 mb-2">
    <fieldset>
        <legend class="h6">{{{{form.{col_name}.label}}}}</legend>
        {{% for radio in form.{col_name} %}}
        <div class="form-check">
            <label for="{{{{ radio.id_for_label }}}}">
                <span class="radio">{{{{ radio.tag }}}}</span>
                {{{{ radio.choice_label }}}}
            </label>
        </div>
        {{% endfor %}}
    </fieldset>
</div>
    """
