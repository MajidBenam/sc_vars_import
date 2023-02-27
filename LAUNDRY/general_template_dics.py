
MYINT = ['IntegerField', 'NumberInput']
MYDEC = ['DecimalField', 'NumberInput']
MYTXT = ['CharField', 'TextInput']
# for these we need, the pandas dfs to smartly select the choices, put them in a tuple or list
MYTXT_CH = ['CharField', 'Select']
MYFOREIGN = ['ForeignKey', 'Select']


def tuple_choices_maker_2(my_new_list_of_choices, choice_name):
    my_tuple_choices = []
    str_mid_list = []
    the_name_of_the_tuple = f"{choice_name.upper()}_CHOICES"
    str_top = f"{the_name_of_the_tuple} = (\n"
    str_bot = ")\n\n"

    for item in my_new_list_of_choices:
        #goodie = v[good_key]["colname"]
        str_mid_list.append(f"('{item}', '{item}'),\n")
        str_mid = "".join(str_mid_list)
    full_string = str_top + str_mid + str_bot
    my_tuple_choices.append(full_string)        
                       
    # take care of beginning and end
    my_tuple_choices.insert(0, f"\n##### tuple choices for  {choice_name}.\n")
    my_tuple_choices_str = "".join(my_tuple_choices)
    return the_name_of_the_tuple, my_tuple_choices_str

#'continuity', 'continuation', 'Continuation', 'contination', 'Continuity', 'continunity', 


degree_of_centralization_CHOICES = ['loose', 'confederated state', 'unitary state', 'nominal', 'confederate state', 'quasi-polity', 'suspected unknown', 'none', 'unknown', 'confederation', 'polity', 'NO_VALUE_ON_WIKI', 'nominal allegiance', 'unitary', ]

supra_polity_relations_CHOICES =  ['none', 'vassalage', 'alliance', 'nominal allegiance', 'suspected unknown', 'nominal', 'personal union', 'NO_VALUE_ON_WIKI', 'unknown', 'Nominal', 'Alliance', 'uncoded',]

language_CHOICES = ['Pashto', 'Persian', 'Greek', 'Bactrian', 'Sogdian', 'Pahlavi', 'Brahmi', 'Kharoshthi', 'Tocharian', 'Chinese', 'archaic Chinese', 'Xiangxi', 'Qiandong', 'Chuanqiandian', 'Hmong-Mien', 'Hmongic', 'Middle Chinese', 'Jurchen', 'Khitan', 'Xianbei', 'Manchu language', 'Mongolian language', 'Atanque', 'Shuar', 'Arabic', 'suspected unknown', 'NO_VALUE_ON_WIKI', 'Demotic', 'Ancient Egyptian', 'Late Egyptian', 'demotic Egyptian', 'Castilian Spanish', 'Chuukese', 'French', 'Langues dOil', 'Occitan', 'Latin', 'Old Frankish', 'Germanic', 'Gallic', 'Gaulish', 'English', 'Akan', 'Twi', 'Doric Greek', 'Minoan', 'Early Greek', 'Eteocretan', 'Old Hawaiian', 'Hawaiian', 'Iban', 'Sanskrit', 'Old Javanese', 'Middle Javanese', 'Javanese', 'Canaanite', 'Aramaic', 'Hebrew', 'Kannada', 'Urdu', 'A’chik', 'Prakrit', 'Telugu', 'Tamil', 'Akkadian', 'Sumerian', 'Amorite', 'Old Babylonian', 'Mesopotamian Religions', 'Old Persian', 'Elamite', 'Egyptian', 'Old Elamite', 'Mongolian', 'native Iranian languages', 'Turkic', 'Turkish', 'Babylonian', 'Hurrian', 'Proto-Elamite', 'Old Norse', 'Italian', 'Middle Japanese', 'Old Japanese', 'Late Old Japanese', 'Japanese', 'Early Modern Japanese', 'Old Turkic', 'Iranian', 'Old Khmer', 'Mon', 'Tai', 'Khmer', 'Pali', 'Phoenician', 'Berber', 'Spanish', 'Portuguese', 'Bambara', 'Mande', 'Songhay', 'Russian', 'Georgian', 'Armenian', 'Kereid', 'Tatar', 'Naimans', 'Khalkha', 'Rouran', 'Xiongnu', 'Oirat', 'Zapotec', 'Icelandic', 'Aymara', 'Puquina', 'Quechua', 'Orokaiva', 'unknown', 'Sindhi', 'Punjabi', 'Sakha (Yakut)', 'Merotic', 'Coptic', 'Thai', 'Proto-Indo-European language', 'Nesite', 'Luwian', 'Hattic', 'Hittite', 'Old Assyrian dialect of Akkadian', 'Indo-European language', 'Lydian', 'Ottoman Turkish', 'Phrygian', 'Miami Illinois', 'Cayuga', 'Mohawk', 'Oneida', 'Onondaga', 'Seneca', 'Tuscarora', 'Middle Mongolian', 'Ancient Iranian', 'Chagatai Turkish', 'Sabaic', 'Mainic', 'Qatabanic', 'Hadramawtic', 'Old Arabic']

# Done Merged (language_genus and linguistic_family)
linguistic_family_CHOICES = ['Indo-European', 'Sino-Tibetan', 'NO_VALUE_ON_WIKI', 'Tungusic', 'Altaic', 'Mongolic', 'Chibcha', 'Chicham', 'Afro-Asiatic', 'Oceanic-Austronesian', 'Celtic', 'Niger-Congo', 'Kwa', 'Hamito-Semitic', 'Austronesian', 'Malayo-Polynesian', 'Semitic', 'Indo-Iranian', 'Dravidian', 'isolate language', 'West Semetic', 'isolate', 'suspected unknown', 'language isolate', 'none', 'Germanic', 'Japonic', 'Turkic', 'Austro-Asiatic, Mon-Khmer', 'Austro-Asiatic', 'unknown', 'Mande', 'Songhay', 'Oghuz', 'Kartvelian', 'Manchu-Tungusic', 'Proto-Mongolic', 'Otomanguean', 'Proto-Otomanguean', 'Mixe-Zoquean', 'Aymaran', 'Quechuan', 'Papuan Languages', 'Tai-Kadai', 'Algonquian', 'Iroquois', 'Iranian']

# Done Merged
religion_genus_CHOICES = ['Zoroastrianism', 'Graeco-Bactrian Religions', 'Buddhism', 'Christianity', 'Islam', 'Mongolian Shamanism', 'Hittite Religions', 'Ismaili', 'Lydian Religions', 'Chinese State Religion', 'Egyptian Religions', 'Ancient Iranian Religions', 'Hellenistic Religions', 'Hephthalite Religions', 'Manichaeism', 'Ancient East Asian Religion', 'Jain Traditions', 'Xiongnu Religions', 'Roman State Religions', 'Shinto', 'Phrygian Religions', 'Mesopotamian Religions', 'Hinduism', 'Ancient Javanese Religions', 'Confucianism',]

# Done Merged
religion_family_CHOICES = ['Saivist Traditions', 'Assyrian Religions', 'Republican Religions', 'Imperial Confucian Traditions', 'Shii', 'Bhagavatist Traditions', 'Sunni', 'Vedist Traditions', 'Saivist', 'Islam', 'Chinese Folk Religion', 'Semitic', 'Vaisnava Traditions', 'Ptolemaic Religion', 'Vedic Traditions', 'Japanese Buddhism', 'Orthodox', 'Vaishnava Traditions', 'Shang Religion', 'Atenism', 'Mahayana', 'suspected unknown', 'Japanese State Shinto', 'Saiva Traditions', 'Sufi', 'Chinese Buddhist Traditions', 'Arian', 'Shia', 'Catholic', 'Western Zhou Religion', 'Imperial Cult', 'Theravada', 'Seleucid Religion',]

# Done Merged
religion_CHOICES = ['Islam', 'Shadhil', 'Karrami', 'Hanafi', 'Mevlevi', 'Ismaili', 'Shafii', 'Shia', 'Twelver', 'Byzantine Orthodox', 'Bektasi', 'NO_VALUE_ON_WIKI', 'Sunni', 'Roman Catholic', ]

relationship_to_preceding_entity_CHOICES = ['continuity', 'elite migration', 'cultural assimilation', 'continuation', 'indigenous revolt', 'replacement', 'population migration', 'hostile', 'disruption/continuity', 'continuity/discontinuity', 'NO_VALUE_ON_WIKI', 'suspected unknown', 'vassalage', 'not applicable',]
################
COL_TEMPLATE_DIC = {'colname': None,
 'dtype': None,
 'varname': None,
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


# NOTE: Everything needs a Seshat Descripton of the kind we had for HS, so we will add comment to allllllllll models.
# NOTE: Everything needs Polity
# Maybe we can keep needsSeshatcommon True for everything and then playaround in the viewws and templates to hide the years and stuff (for RAs for exampel)

############_ra_###############
VAR_GENERAl_researchassistant_TEMPLATE_DIC = {
'varname': 'researchassistant',
  'cols': 1,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The RA(s) who worked on a polity.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "Staff", # Hier 
 }

COL_GENERAl_ra_TEMPLATE_DIC = [{'colname': "full_name",
 'dtype': MYTXT,
 'varname': 'researchassistant', # key
 'col_exp': "The full name of the RA.",
 'col_exp_source': None,
 'max_digits': 70,
 'null_meaning': None}]

##############_utmzone_#############
VAR_GENERAl_utmzone_TEMPLATE_DIC = {
'varname': 'utmzone',
  'cols': 1,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The UTM Zone of a polity.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_utmzone_TEMPLATE_DIC = [{'colname': "utm_zone",
 'dtype': MYTXT,
 'varname': 'utmzone', # key
 'col_exp': "The details of UTM_ZONE.",
 'col_exp_source': None,
 'max_digits': 5,
 'null_meaning': "No_Value_Provided_in_Old_Wiki"}]


##############_originalpolityname_#############
VAR_GENERAl_originalpolityname_TEMPLATE_DIC = {
'varname': 'originalpolityname',
  'cols': 1,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The original name of a polity.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_originalpolityname_TEMPLATE_DIC = [{'colname': "original_name",
 'dtype': MYTXT,
 'varname': 'originalpolityname', # key
 'col_exp': "The details of original_name.",
 'col_exp_source': None,
 'max_digits': 100,
 'null_meaning': "No_Value_Provided_in_Old_Wiki"}]

##############_alternativepolityname_#############
VAR_GENERAl_alternativepolityname_TEMPLATE_DIC = {
'varname': 'alternativepolityname',
  'cols': 1,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The alternative name of a polity.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_alternativepolityname_TEMPLATE_DIC = [{'colname': "alternative_name",
 'dtype': MYTXT,
 'varname': 'alternativepolityname', # key
 'col_exp': "The details of alternative_name.",
 'col_exp_source': None,
 'max_digits': 100,
 'null_meaning': "No_Value_Provided_in_Old_Wiki"}]


##############_peakyears_#############
VAR_GENERAl_peakyears_TEMPLATE_DIC = {
'varname': 'peakyears',
  'cols': 2,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The alternative name of a polity.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_peakyears_TEMPLATE_DIC = [{'colname': "peak_year_from",
 'dtype': MYINT,
 'varname': 'peakyears', # key
 'col_exp': "The beginning of the peak year for a polity.",
 'col_exp_source': None,
 'null_meaning': "No_Value_Provided_in_Old_Wiki"},
 
 {'colname': "peak_year_to",
 'dtype': MYINT,
 'varname': 'peakyears', # key
 'col_exp':  "The end of the peak year for a polity.",
 'col_exp_source': None,
 'null_meaning': "No_Value_Provided_in_Old_Wiki"}]


 ##############_duration_#############
VAR_GENERAl_duration_TEMPLATE_DIC = {
'varname': 'duration',
  'cols': 2,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The alternative name of a polity.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_duration_TEMPLATE_DIC = [{'colname': "polity_year_from",
 'dtype': MYINT,
 'varname': 'duration', # key
 'col_exp': "The beginning year for a polity.",
 'col_exp_source': None,
 'null_meaning': "No_Value_Provided_in_Old_Wiki"},
 
 {'colname': "polity_year_to",
 'dtype': MYINT,
 'varname': 'duration', # key
 'col_exp':  "The end year for a polity.",
 'col_exp_source': None,
 'null_meaning': "No_Value_Provided_in_Old_Wiki"}]


 

 ##############_degree_of_centralization_#############
VAR_GENERAl_degreeofcentralization_TEMPLATE_DIC = {
'varname': 'degreeofcentralization',
  'cols': 1,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The degree of centralization of a polity.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_degree_of_centralization_TEMPLATE_DIC = [{'colname': "degree_of_centralization",
 'dtype': MYTXT_CH,
 'varname': 'degreeofcentralization', # key
 'col_exp': "The details of degree_of_centralization.",
 'col_exp_source': None,
 'max_digits': 50,
'choices': tuple_choices_maker_2(degree_of_centralization_CHOICES, "degree_of_centralization")[0],
'null_meaning': "No_Value_Provided_in_Old_Wiki"}]


  ##############_suprapolityrelations_#############
VAR_GENERAl_suprapolityrelations_TEMPLATE_DIC = {
'varname': 'suprapolityrelations',
  'cols': 1,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The supra polity relations of a polity.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_suprapolityrelations_TEMPLATE_DIC = [{'colname': "supra_polity_relations",
 'dtype': MYTXT_CH,
 'varname': 'suprapolityrelations', # key
 'col_exp': "The details of supra polity relations.",
 'col_exp_source': None,
 'max_digits': 50,
 'choices': tuple_choices_maker_2(supra_polity_relations_CHOICES, "supra_polity_relations")[0],
 'null_meaning': "No_Value_Provided_in_Old_Wiki"}]

 ############_capital_###############
VAR_GENERAl_politycapital_TEMPLATE_DIC = {
'varname': 'politycapital',
  'cols': 1,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The capital or the largest settlement of a polity.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_politycapital_TEMPLATE_DIC = [{'colname': "capital",
 'dtype': MYTXT,
 'varname': 'politycapital', # key
 'col_exp': "The capital or the largest settlement of a polity.",
 'col_exp_source': None,
 'max_digits': 70,
 'null_meaning': "This polity did not have a capital or the largest settlement."}]


  ############_language_###############
VAR_GENERAl_politylanguage_TEMPLATE_DIC = {
'varname': 'politylanguage',
  'cols': 1,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The language or the largest settlement of a polity.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_politylanguage_TEMPLATE_DIC = [{'colname': "language",
 'dtype': MYTXT_CH,
 'varname': 'politylanguage', # key
 'col_exp': "The language of a polity.",
 'col_exp_source': None,
 'max_digits': 70,
 'choices': tuple_choices_maker_2(language_CHOICES, "language")[0],
 'null_meaning': "This polity did not have a language."}]

  ############_linguisticfamily_###############
VAR_GENERAl_politylinguisticfamily_TEMPLATE_DIC = {
'varname': 'politylinguisticfamily',
  'cols': 1,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The linguistic family of a polity.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_politylinguisticfamily_TEMPLATE_DIC = [{'colname': "linguistic_family",
 'dtype': MYTXT_CH,
 'varname': 'politylinguisticfamily', # key
 'col_exp': "The linguistic family of a polity.",
 'col_exp_source': None,
 'max_digits': 70,
 'choices': tuple_choices_maker_2(linguistic_family_CHOICES, "linguistic_family")[0],
 'null_meaning': "This polity did not have a linguistic family."}]

  ############_languagegenus_###############
VAR_GENERAl_politylanguagegenus_TEMPLATE_DIC = {
'varname': 'politylanguagegenus',
  'cols': 1,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The language genus of a polity.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_politylanguagegenus_TEMPLATE_DIC = [{'colname': "language_genus",
 'dtype': MYTXT_CH,
 'varname': 'politylanguagegenus', # key
 'col_exp': "The language genus of a polity.",
 'col_exp_source': None,
 'max_digits': 70,
 'choices': tuple_choices_maker_2(linguistic_family_CHOICES, "linguistic_family")[0],
 'null_meaning': "This polity did not have a language Genus."}]

  ############_religiongenus_###############
VAR_GENERAl_polityreligiongenus_TEMPLATE_DIC = {
'varname': 'polityreligiongenus',
  'cols': 1,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The religion genus of a polity.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_polityreligiongenus_TEMPLATE_DIC = [{'colname': "religion_genus",
 'dtype': MYTXT_CH,
 'varname': 'polityreligiongenus', # key
 'col_exp': "The religion genus of a polity.",
 'col_exp_source': None,
 'max_digits': 70,
 'choices': tuple_choices_maker_2(religion_genus_CHOICES, "religion_genus")[0],
 'null_meaning': "This polity did not have a religion genus."}]

  ############_religionfamily_###############
VAR_GENERAl_polityreligionfamily_TEMPLATE_DIC = {
'varname': 'polityreligionfamily',
  'cols': 1,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The religion family of a polity.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_polityreligionfamily_TEMPLATE_DIC = [{'colname': "religion_family",
 'dtype': MYTXT_CH,
 'varname': 'polityreligionfamily', # key
 'col_exp': "The religion family of a polity.",
 'col_exp_source': None,
 'max_digits': 70,
 'choices': tuple_choices_maker_2(religion_family_CHOICES, "religion_family")[0],
 'null_meaning': "This polity did not have a religion family."}]


  ############_religion_###############
VAR_GENERAl_polityreligion_TEMPLATE_DIC = {
'varname': 'polityreligion',
  'cols': 1,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The religion of a polity.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_polityreligion_TEMPLATE_DIC = [{'colname': "religion",
 'dtype': MYTXT_CH,
 'varname': 'polityreligion', # key
 'col_exp': "The religion of a polity.",
 'col_exp_source': None,
 'max_digits': 70,
 'choices': tuple_choices_maker_2(religion_CHOICES, "religion")[0],
 'null_meaning': "This polity did not have a religion."}]


  ############_relationship_to_preceding_entity_###############
VAR_GENERAl_polityrelationship_to_preceding_entity_TEMPLATE_DIC = {
'varname': 'polityrelationshiptoprecedingentity',
  'cols': 1,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The polity relationship to preceding (quasi)polity", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_polityrelationship_to_preceding_entity_TEMPLATE_DIC = [{'colname': "relationship_to_preceding_entity",
 'dtype': MYTXT_CH,
 'varname': 'polityrelationshiptoprecedingentity', # key
 'col_exp': "The polity relationship to preceding (quasi)polity",
 'col_exp_source': None,
 'max_digits': 70,
 'choices': tuple_choices_maker_2(relationship_to_preceding_entity_CHOICES, "relationship_to_preceding_entity")[0],
 'null_meaning': "This polity did not have a relationship to preceding (quasi)polity"}]


 ############_preceding_entity_###############
VAR_GENERAl_politypreceding_entity_TEMPLATE_DIC = {
'varname': 'polityprecedingentity',
  'cols': 1,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The preceding entity of a polity.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_politypreceding_entity_TEMPLATE_DIC = [{'colname': "preceding_entity",
 'dtype': MYTXT,
 'varname': 'polityprecedingentity', # key
 'col_exp': "The preceding entity or the largest settlement of a polity.",
 'col_exp_source': None,
 'max_digits': 70,
 'null_meaning': "This polity did not have a preceding entity."}]


  ############_succeeding_entity_###############
VAR_GENERAl_politysucceeding_entity_TEMPLATE_DIC = {
'varname': 'politysucceedingentity',
  'cols': 1,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The succeeding entity of a polity.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_politysucceeding_entity_TEMPLATE_DIC = [{'colname': "succeeding_entity",
 'dtype': MYTXT,
 'varname': 'politysucceedingentity', # key
 'col_exp': "The succeeding entity or the largest settlement of a polity.",
 'col_exp_source': None,
 'max_digits': 70,
 'null_meaning': "This polity did not have a succeeding entity."}]

   ############_supracultural_entity_###############
VAR_GENERAl_politysupracultural_entity_TEMPLATE_DIC = {
'varname': 'politysupraculturalentity',
  'cols': 1,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The supracultural entity of a polity.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_politysupracultural_entity_TEMPLATE_DIC = [{'colname': "supracultural_entity",
 'dtype': MYTXT,
 'varname': 'politysupraculturalentity', # key
 'col_exp': "The supracultural entity or the largest settlement of a polity.",
 'col_exp_source': None,
 'max_digits': 100,
 'null_meaning': "This polity did not have a supracultural entity."}]


##############_scale_of_supra_cultural_interaction_#############
VAR_GENERAl_scaleofsupraculturalinteraction_TEMPLATE_DIC = {
'varname': 'scaleofsupraculturalinteraction',
  'cols': 2,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The scale_of_supra_cultural_interaction of a polity.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_scaleofsupraculturalinteraction_TEMPLATE_DIC = [
{'colname': "scale_from",
 'dtype': MYINT,
 'varname': 'scaleofsupraculturalinteraction', # key
 'col_exp': "The lower scale of supra cultural interactionfor a polity.",
 'col_exp_source': None,
  'units': "km squared",
 'min': 0,
 'null_meaning': "No_Value_Provided_in_Old_Wiki"},
 
 {'colname': "scale_to",
 'dtype': MYINT,
 'varname': 'scaleofsupraculturalinteraction', # key
 'col_exp':  "The upper scale of supra cultural interactionfor a polity.",
 'col_exp_source': None,
  'units': "km squared",
 'min': 0,
 'null_meaning': "No_Value_Provided_in_Old_Wiki"}]


 ############_alternatereligiongenus_###############
VAR_GENERAl_polityalternatereligiongenus_TEMPLATE_DIC = {
'varname': 'polityalternatereligiongenus',
  'cols': 1,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The alternate religion genus of a polity.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_polityalternatereligiongenus_TEMPLATE_DIC = [{'colname': "alternate_religion_genus",
 'dtype': MYTXT_CH,
 'varname': 'polityalternatereligiongenus', # key
 'col_exp': "The alternate religion genus of a polity.",
 'col_exp_source': None,
 'max_digits': 70,
 'choices': tuple_choices_maker_2(religion_genus_CHOICES, "religion_genus")[0],
 'null_meaning': "This polity did not have a alternatereligion genus."}]


 ############_alternatereligionfamily_###############
VAR_GENERAl_polityalternatereligionfamily_TEMPLATE_DIC = {
'varname': 'polityalternatereligionfamily',
  'cols': 1,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The alternate religion family of a polity.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_polityalternatereligionfamily_TEMPLATE_DIC = [{'colname': "alternate_religion_family",
 'dtype': MYTXT_CH,
 'varname': 'polityalternatereligionfamily', # key
 'col_exp': "The alternate religion family of a polity.",
 'col_exp_source': None,
 'max_digits': 70,
 'choices': tuple_choices_maker_2(religion_family_CHOICES, "religion_family")[0],
 'null_meaning': "This polity did not have a alternate religion family."}]


  ############_alternatereligion_###############
VAR_GENERAl_polityalternatereligion_TEMPLATE_DIC = {
'varname': 'polityalternatereligion',
  'cols': 1,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The alternate religion  of a polity.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_polityalternatereligion_TEMPLATE_DIC = [{'colname': "alternate_religion",
 'dtype': MYTXT_CH,
 'varname': 'polityalternatereligion', # key
 'col_exp': "The alternate religion of a polity.",
 'col_exp_source': None,
 'max_digits': 70,
 'choices': tuple_choices_maker_2(religion_CHOICES, "religion")[0],
 'null_meaning': "This polity did not have a alternate religion ."}]

  ############_expert_###############
VAR_GENERAl_polityexpert_TEMPLATE_DIC = {
'varname': 'polityexpert',
  'cols': 1,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The expert of a polity.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_polityexpert_TEMPLATE_DIC = [{'colname': "expert",
 'dtype': MYFOREIGN,
 'varname': 'polityexpert', # key
 'col_exp': "The expert of a polity.",
 'col_exp_source': None,
 'foreign_key': "SeshatExpert",
 'foreign_key_related_name': "seshat_expert",
 'null_meaning': "This polity did not have an expert."}]


  ############_editor_###############
VAR_GENERAl_polityeditor_TEMPLATE_DIC = {
'varname': 'polityeditor',
  'cols': 1,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The editor of a polity.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_polityeditor_TEMPLATE_DIC = [{'colname': "editor",
 'dtype': MYFOREIGN,
 'varname': 'polityeditor', # key
 'col_exp': "The editor of a polity.",
 'col_exp_source': None,
'foreign_key': "SeshatExpert",
 'foreign_key_related_name': "seshat_editor",
 'null_meaning': "This polity did not have an editor."}]

 ##############_religioustradition_#############
VAR_GENERAl_religioustradition_TEMPLATE_DIC = {
'varname': 'religioustradition',
  'cols': 1,
  'needsSeshatCommon': True,
 'db_name': "general", # Hier
 'main_desc': "The details of religious traditions.", # Hier
 'main_desc_source': None, # Hier
 'section': "General Variables", # Hier
 'subsection': "General", # Hier 
 }

COL_GENERAl_religioustradition_TEMPLATE_DIC = [{'colname': "religious_tradition",
 'dtype': MYTXT,
 'varname': 'religioustradition', # key
 'col_exp': "The details of religious traditions.",
 'col_exp_source': None,
 'max_digits': 100,
 'null_meaning': "No_Value_Provided_in_Old_Wiki"}]