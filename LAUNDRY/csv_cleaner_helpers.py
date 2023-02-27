import pandas as pd

import json
import copy
import re

import numpy as np

COL_TEMPLATE_DIC = {'colname': None,
 'dtype': None,
 'varname': None, # key
 'col_exp': None,
 'col_exp_source': None,
  'col_description': None,
 'units': None,
 'min': None,
 'max': None,
 'scale': None,
 'decimal_places': None,
 'max_digits': None,
 'choices': None,
 'foreign_key': None,
 'foreign_key_related_name': None,
 'null_meaning': None}

VAR_TEMPLATE_DIC = {
'varname': None,
  'cols': None,
  'needsSeshatCommon': None,
 'db_name': None, # Hier
 'main_desc': None, # Hier
 'main_desc_source': None, # Hier
 'section': None, # Hier
 'subsection': None, # Hier 
 }



###### yearRegEx finder:

def is_there_years_here(my_str):
    """"
    INPUT: Receives a _str and decided on the BCE and Ce information inside it and returns a [-123, 498] list of values for year_from and year_to vals
    """
    print("______")
    print(my_str)
    upper_case_str = my_str.upper().strip()
    my_catches = re.findall('(-?\d{1,4})[ ]{0,1}(B*CE*)*[-|_| ](\d{1,4})[ ]{0,1}(B*CE*)*', upper_case_str)
    if len(my_catches) > 1:
        print(f"Catches are more than 1: {len(my_catches)}")
    elif len(my_catches) == 0:
        # try the singöe year option:
        my_catches_single  = re.findall('(-?\d{1,4})[ ]{0,1}(B*CE*)*', upper_case_str)
        if len(my_catches_single) == 1:
            year_from = my_catches_single[0][0]
            year_from_tag = my_catches_single[0][1]
            if year_from_tag == "BCE":
                print(f"YEAR_FROM: {int(year_from)}, SINGLE!!!")
                return [-int(year_from), -int(year_from)]
            elif year_from_tag == "CE":
                print(f"YEAR_FROM: {int(year_from)}, SINGLE!!!")
                return [int(year_from), int(year_from)]
            else:
                print("Weird TAg for year_from")
        else:
            print(f"Bad number of matches: {len(my_catches)}")
        return -88888
    else:
        # year_from
        year_from = my_catches[0][0]
        year_from_tag = my_catches[0][1]
        year_to = my_catches[0][2]
        year_to_tag = my_catches[0][3]
        if "-" in year_from:
            print(f"Attention. the value year_from has a negative value: {year_from}")
        if "-" in year_to:
            print(f"Attention. the value year_to has a negative value: {year_to}")
        if year_from_tag not in ["CE", "BCE", ""]:
            print(f"Attention. the value year_from_tag has a weird value: {year_from_tag}")
        if year_to_tag not in ["CE", "BCE", ""]:
            print(f"Attention. the value year_to_tag has a weird value: {year_to_tag}")
        if year_from_tag in ["CE", "", " "] and year_to_tag in ["CE", "", " "]:
            print(f"YEAR_FROM: {int(year_from)}, YEAR_TO: {int(year_to)}")
            return [int(year_from), int(year_to)]
        if year_from_tag in ["BCE", "", " "] and year_to_tag in ["BCE",]:
            print(f"YEAR_FROM: {-int(year_from)}, YEAR_TO: {-int(year_to)}")
            return [-int(year_from), -int(year_to)]
        if year_from_tag in ["", " "] and year_to_tag in ["BCE",]:
            print(f"YEAR_FROM: {-int(year_from)}, YEAR_TO: {-int(year_to)}")
            return [-int(year_from), -int(year_to)]
        if year_from_tag in ["BCE",] and year_to_tag in ["CE", "", " "]:
            print(f"YEAR_FROM: {-int(year_from)}, YEAR_TO: {int(year_to)}")
            return [-int(year_from), int(year_to)]

    return -99999

def remove_year_range(a_str):
    """
    INPUT:  A string that potentially contans some year info
    RETURNS: the same input with the year values stripped off of it.
    """
    my_new_str = re.sub('(-?\d{1,4})[ ]{0,1}(B*CE*)*[-|_| ](\d{1,4})[ ]{0,1}(B*CE*)*', "", a_str)
    while "  " in my_new_str:
        my_new_str  = my_new_str.replace("  ", " ").strip()
    return my_new_str



def convert_crisisdb_vars_dic_to_two_dfs(db_json_file):
    # let's create the mother meta_dfs we need for taking care of the data read from almost anywhere 
    meta_cols_in_variables = [
        "colname", "dtype", "varname", "col_exp", "col_exp_source", "units", "min", "max", "scale", 
        "decimal_places", "max_digits", "choices", "foreign_key", "foreign_key_related_name", "null_meaning", 
    ]

    meta_variables = [
        "varname", "db_name", "main_desc", "main_desc_source", "notes", "cols", "section", "subsection", "needsSeshatCommon",
    ]

    df_variables = pd.DataFrame(columns=meta_variables)
    df_cols_in_variables = pd.DataFrame(columns=meta_cols_in_variables)



    with open(db_json_file) as json_file:
        crisisdb_data = json.load(json_file)

    for variable, inner_data in crisisdb_data.items():
        # dic to be appended
        my_var_dic = {
            "varname": variable,
            "db_name": "crisisdb",
            "needsSeshatCommon": inner_data.get("needsSeshatCommon"),
            "main_desc": inner_data["main_desc"],
            "main_desc_source": inner_data["main_desc_source"],
            "notes": inner_data["notes"],
            "cols": inner_data["cols"],
            "section": inner_data["section"],
            "subsection": inner_data["subsection"],
        }
        df_variables = df_variables.append(my_var_dic, ignore_index=True)
        
        number_of_cols = int(inner_data["cols"])
        for i in range(1, number_of_cols +1):
            column_key = "col" + str(i)
            my_col_dic = copy.deepcopy(inner_data[column_key])
            my_col_dic["colname"] = inner_data[column_key]["varname"]
            my_col_dic["varname"] = variable
            my_col_dic["null_meaning"]: inner_data["null_meaning"]
            my_col_dic["col_exp"]: inner_data[column_key]["var_exp"]
            my_col_dic["col_exp_source"]: inner_data[column_key]["var_exp_source"]
            del my_col_dic["var_exp_source"]
            del my_col_dic["var_exp"]

            df_cols_in_variables = df_cols_in_variables.append(my_col_dic, ignore_index=True)

    return df_variables, df_cols_in_variables


def convert_two_dfs_to_python_vars_dic(df_vars, df_cols, my_db_name="general"):
    df_vars = df_vars.where(pd.notnull(df_vars), None)
    df_cols = df_cols.where(pd.notnull(df_cols), None)
    vars_dic = df_vars.to_dict('index')
    cols_dic = df_cols.to_dict('index')
    final_vars_dic = {}
    for index, main_var_dic in vars_dic.items():
        if main_var_dic["varname"] not in final_vars_dic.keys():
            final_vars_dic[main_var_dic["varname"]] = copy.deepcopy(main_var_dic)
            final_vars_dic[main_var_dic["varname"]]["db_name"] = my_db_name
            del final_vars_dic[main_var_dic["varname"]]["varname"]

            done_cols = []
            hits = 0
            for col_index, col_dic in cols_dic.items():
                if col_dic['colname'] in done_cols:
                    break
                if col_dic['varname'] == main_var_dic['varname']:
                    hits = hits + 1 
                    column_key = "col" + str(hits)
                    final_vars_dic[main_var_dic["varname"]][column_key] = {}
                    for col_key, col_val in col_dic.items():
                        if col_val:
                            final_vars_dic[main_var_dic["varname"]][column_key][col_key] = col_val
                    done_cols.append(col_dic['colname'])
                    #print(done_cols)

    return final_vars_dic


# add a row to the  df 
def meta_empty_dfs():
    # let's create the mother meta_dfs we need for taking care of the data read from almost anywhere 
    meta_cols_in_variables = [
        "colname", "dtype", "varname", "col_exp", "col_exp_source", "units", "min", "max", "scale", 
        "decimal_places", "max_digits", "choices", "foreign_key", "foreign_key_related_name", "null_meaning", 
    ]

    meta_variables = [
        "varname", "db_name", "main_desc", "main_desc_source", "notes", "cols", "section", "subsection", "needsSeshatCommon",
    ]

    df_variables = pd.DataFrame(columns=meta_variables)
    df_cols_in_variables = pd.DataFrame(columns=meta_cols_in_variables)

    return df_variables, df_cols_in_variables

def append_to_df(df, my_dic):
    df = df.append(my_dic, ignore_index=True)
    return df






#vars_dic = {}
def vars_dic_entry_maker(var_name,
                         df_var,
                        my_ints_dic,
                         my_floats_dic,
                         my_chars_dic,
                         my_text_selects_dic,
                         my_foreign_keys,
                         section_name,
                         subsection_name,
                         notes = "Notes on the Variable",
                         main_desc = "Main description of the Variable",
                         main_desc_source = "",
                        null_meaning = "The value is not available."):
    import json
    try:
        with open('/home/majid/dev/seshat/jim_metadata/resulting_vars_dic.json', 'r') as json_file:
            vars_dic = json.load(json_file)
    except:
        vars_dic = {}
    # to_Form field converter
    MYINT = ['IntegerField', 'NumberInput']
    MYDEC = ['DecimalField', 'NumberInput']
    MYTXT = ['CharField', 'TextInput']
    # for these we need, the pandas dfs to smartly select the choices, put them in a tuple or list
    MYTXT_CH = ['CharField', 'Select']
    MYFOREIGN = ['ForeignKey', 'Select']

#     my_ints = []
#     my_floats = ['longitude', 'latitude', 'elevation']
#     my_chars = []
#     my_text_selects = ['sub_category', 'magnitude', 'duration']
    number_of_columns = len(my_ints_dic) + len(my_floats_dic) + len(my_chars_dic) + len(my_text_selects_dic) + len(my_foreign_keys)
    if notes == "Notes on the Variable":
        notes = "Notes for the Variable " + var_name + " are missing!"
    if main_desc == "Main description of the Variable":
        main_desc = "Main Descriptions for the Variable " + var_name + " are missing!"
    var_dic = {
        "notes": notes,
        "main_desc": main_desc,
        "main_desc_source": main_desc_source,
        "cols": number_of_columns,
        "section": section_name,
        "subsection": subsection_name,
        "null_meaning": null_meaning,
    }
    col_num = 1
    for col_name in list(df_var.columns):
        if col_name in my_ints_dic.keys():
            print("Hit me: ", col_name)
            good_key = "col" + str(col_num)
            var_dic[good_key] = {
                'dtype': MYINT,
                'varname': col_name,
                'var_exp': my_ints_dic[col_name].get('var_exp', "No Explanations Provided."),
                'units': my_ints_dic[col_name].get('units', "No Units Provided."),
                'min': my_ints_dic[col_name].get('min', None),
                'max': my_ints_dic[col_name].get('max', None),
                'scale': my_ints_dic[col_name].get('scale', 1),
                'var_exp_source': my_ints_dic[col_name].get('var_exp_source', None),
                }
            col_num = col_num + 1
            continue
        if col_name in my_floats_dic.keys():
            good_key = "col" + str(col_num)
            var_dic[good_key] = {
                'dtype': MYDEC,
                'varname': col_name,
                'var_exp': my_floats_dic[col_name].get('var_exp', "No Explanations Provided."),
                'units': my_floats_dic[col_name].get('units', "No Units Provided."),
                'min': my_floats_dic[col_name].get('min', None),
                'max': my_floats_dic[col_name].get('max', None),
                'scale': my_floats_dic[col_name].get('scale', 1),
                'decimal_places': my_floats_dic[col_name].get('decimal_places', 0),
                'max_digits': my_floats_dic[col_name].get('decimal_numbers', 20),
                'var_exp_source': my_floats_dic[col_name].get('var_exp_source', None),
                }
            col_num = col_num + 1
            continue
        if col_name in my_chars_dic.keys():
            good_key = "col" + str(col_num)
            var_dic[good_key] = {
                'dtype': MYTXT,
                'varname': col_name,
                'var_exp': my_chars_dic[col_name].get('var_exp', "No Explanations Provided."),
                'var_exp_source': my_chars_dic[col_name].get('var_exp_source', None),
                }
            col_num = col_num + 1
            continue
        if col_name in my_text_selects_dic.keys():
            my_choices = list(df_var[col_name].unique())
            good_key = "col" + str(col_num)
            var_dic[good_key] = {
                'dtype': MYTXT_CH,
                'varname': col_name,
                'var_exp': my_text_selects_dic[col_name].get('var_exp', "No Explanations Provided."),
                'var_exp_source': my_text_selects_dic[col_name].get('var_exp_source', None),
                'choices': my_choices,
                }
            col_num = col_num + 1
            continue
        if col_name in my_foreign_keys.keys():
            good_key = "col" + str(col_num)
            var_dic[good_key] = {
                'dtype': MYFOREIGN,
                'varname': col_name,
                'var_exp': my_foreign_keys[col_name].get('var_exp', "No Explanations Provided."),
                'var_exp_source': my_foreign_keys[col_name].get('var_exp_source', None),
                'foreign_key': my_foreign_keys[col_name].get('foreign_key', None),
                'foreign_key_related_name': my_foreign_keys[col_name].get('foreign_key_related_name', None),
                }
            col_num = col_num + 1
            continue
    if var_name in vars_dic.keys():
        print("WARNING: Variable ", var_name, " is already in the list of variables. \n ACTION RECOMMENDED.")
    vars_dic[var_name] = var_dic
    with open('/home/majid/dev/seshat/jim_metadata/resulting_vars_dic.json', 'w') as fp:
        json.dump(vars_dic, fp)
        
def polity_id_decider_qing(df):
    if df['year_from'] > 1795:
        return "CnQingL"
    else:
        return "CnQingE"
        
def add_polity_col(df):
    df["polity_id"] = df.apply(polity_id_decider_qing, axis=1)
    # bring polity_id col to the front of the df:
    backup = df["polity_id"]
    df.drop(labels=["polity_id"], axis=1,inplace = True)
    df.insert(0, 'polity_id', backup)
    return df

def add_year_to(df):
    df["year_to"] = df["year_from"]
    backup = df["year_to"]
    df.drop(labels=["year_to"], axis=1,inplace = True)
    df.insert(2, 'year_to', backup)
    return df

def move_col_to(df, col_name, col_new_index):
    backup = df[col_name]
    df.drop(labels=[col_name], axis=1,inplace = True)
    df.insert(col_new_index, col_name, backup)
    return df

def period_to_year(df, separator,col_name):
    if separator in df[col_name]:
        years =  df[col_name].split(separator)
        year_from = int(years[0])
        year_to = int(years[1])
        return pd.Series([year_from, year_to])
    else:
        return pd.Series([int(df[col_name]), int(df[col_name])])