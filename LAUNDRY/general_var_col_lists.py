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

'continuity', 'continuation', 'Continuation', 'contination', 'Continuity', 'continunity', 


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


ALL_GENERAL_VARS_LIST =[
    {
    'varname': 'researchassistant',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The RA(s) who worked on a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "Staff", # Hier 
    },
    {
    'varname': 'utmzone',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The UTM Zone of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'originalpolityname',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The original name of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'alternativepolityname',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The alternative name of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'peakyears',
    'cols': 2,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The alternative name of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'duration',
    'cols': 2,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The alternative name of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'degreeofcentralization',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The degree of centralization of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'suprapolityrelations',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The supra polity relations of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'politycapital',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The capital or the largest settlement of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'politylanguage',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The language or the largest settlement of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'politylinguisticfamily',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The linguistic family of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'politylanguagegenus',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The language genus of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polityreligiongenus',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The religion genus of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polityreligionfamily',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The religion family of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polityreligion',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The religion of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polityrelationshiptoprecedingentity',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The polity relationship to preceding (quasi)polity", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polityprecedingentity',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The preceding entity of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'politysucceedingentity',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The succeeding entity of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'politysupraculturalentity',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The supracultural entity of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'scaleofsupraculturalinteraction',
    'cols': 2,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The scale_of_supra_cultural_interaction of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polityalternatereligiongenus',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The alternate religion genus of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polityalternatereligionfamily',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The alternate religion family of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polityalternatereligion',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The alternate religion  of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polityexpert',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The expert of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'polityeditor',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The editor of a polity.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    },
    {
    'varname': 'religioustradition',
    'cols': 1,
    'needsSeshatCommon': True,
    'db_name': "general", # Hier
    'main_desc': "The details of religious traditions.", # Hier
    'section': "General Variables", # Hier
    'subsection': "General", # Hier 
    }
]


ALL_GENERAL_COLS_LIST =[
{
    'colname': "polity_ra",
    'dtype': MYFOREIGN,
    'varname': 'researchassistant', # key
    'col_exp': "The RA of a polity.",
    'foreign_key': "SeshatExpert",
    'foreign_key_related_name': "seshat_research_assistant",
    },
    {
    'colname': "utm_zone",
    'dtype': MYTXT,
    'varname': 'utmzone', # key
    'col_exp': "The details of UTM_ZONE.",
    'max_digits': 5,
    'null_meaning': "No_Value_Provided_in_Old_Wiki"
    },
    {
    'colname': "original_name",
    'dtype': MYTXT,
    'varname': 'originalpolityname', # key
    'col_exp': "The details of original_name.",
    'max_digits': 100,
    'null_meaning': "No_Value_Provided_in_Old_Wiki"
    },
    {
    'colname': "alternative_name",
    'dtype': MYTXT,
    'varname': 'alternativepolityname', # key
    'col_exp': "The details of alternative_name.",
    'max_digits': 100,
    'null_meaning': "No_Value_Provided_in_Old_Wiki"
    },
    {
    'colname': "peak_year_from",
    'dtype': MYINT,
    'varname': 'peakyears', # key
    'col_exp': "The beginning of the peak year for a polity.",
    'null_meaning': "No_Value_Provided_in_Old_Wiki"
    },
    {
    'colname': "peak_year_to",
    'dtype': MYINT,
    'varname': 'peakyears', # key
    'col_exp':  "The end of the peak year for a polity.",
    'null_meaning': "No_Value_Provided_in_Old_Wiki"
    },
    {
    'colname': "polity_year_from",
    'dtype': MYINT,
    'varname': 'duration', # key
    'col_exp': "The beginning year for a polity.",
    'null_meaning': "No_Value_Provided_in_Old_Wiki"
    },
    {
    'colname': "polity_year_to",
    'dtype': MYINT,
    'varname': 'duration', # key
    'col_exp':  "The end year for a polity.",
    'null_meaning': "No_Value_Provided_in_Old_Wiki"
    },
    {
    'colname': "degree_of_centralization",
    'dtype': MYTXT_CH,
    'varname': 'degreeofcentralization', # key
    'col_exp': "The details of degree_of_centralization.",
    'max_digits': 50,
    'choices': tuple_choices_maker_2(degree_of_centralization_CHOICES, "degree_of_centralization")[0],
    'null_meaning': "No_Value_Provided_in_Old_Wiki"
    },
    {
    'colname': "supra_polity_relations",
    'dtype': MYTXT_CH,
    'varname': 'suprapolityrelations', # key
    'col_exp': "The details of supra polity relations.",
    'max_digits': 50,
    'choices': tuple_choices_maker_2(supra_polity_relations_CHOICES, "supra_polity_relations")[0],
    'null_meaning': "No_Value_Provided_in_Old_Wiki"
    },
    {
    'colname': "capital",
    'dtype': MYTXT,
    'varname': 'politycapital', # key
    'col_exp': "The capital or the largest settlement of a polity.",
    'max_digits': 70,
    'null_meaning': "This polity did not have a capital or the largest settlement."
    },
    {
    'colname': "language",
    'dtype': MYTXT_CH,
    'varname': 'politylanguage', # key
    'col_exp': "The language of a polity.",
    'max_digits': 70,
    'choices': tuple_choices_maker_2(language_CHOICES, "language")[0],
    'null_meaning': "This polity did not have a language."
    },
    {
    'colname': "linguistic_family",
    'dtype': MYTXT_CH,
    'varname': 'politylinguisticfamily', # key
    'col_exp': "The linguistic family of a polity.",
    'max_digits': 70,
    'choices': tuple_choices_maker_2(linguistic_family_CHOICES, "linguistic_family")[0],
    'null_meaning': "This polity did not have a linguistic family."
    },
    {
    'colname': "language_genus",
    'dtype': MYTXT_CH,
    'varname': 'politylanguagegenus', # key
    'col_exp': "The language genus of a polity.",
    'max_digits': 70,
    'choices': tuple_choices_maker_2(linguistic_family_CHOICES, "linguistic_family")[0],
    'null_meaning': "This polity did not have a language Genus."
    },
    {
    'colname': "religion_genus",
    'dtype': MYTXT_CH,
    'varname': 'polityreligiongenus', # key
    'col_exp': "The religion genus of a polity.",
    'max_digits': 70,
    'choices': tuple_choices_maker_2(religion_genus_CHOICES, "religion_genus")[0],
    'null_meaning': "This polity did not have a religion genus."
    },
    {
    'colname': "religion_family",
    'dtype': MYTXT_CH,
    'varname': 'polityreligionfamily', # key
    'col_exp': "The religion family of a polity.",
    'max_digits': 70,
    'choices': tuple_choices_maker_2(religion_family_CHOICES, "religion_family")[0],
    'null_meaning': "This polity did not have a religion family."
    },
    {
    'colname': "religion",
    'dtype': MYTXT_CH,
    'varname': 'polityreligion', # key
    'col_exp': "The religion of a polity.",
    'max_digits': 70,
    'choices': tuple_choices_maker_2(religion_CHOICES, "religion")[0],
    'null_meaning': "This polity did not have a religion."
    },
    {
    'colname': "relationship_to_preceding_entity",
    'dtype': MYTXT_CH,
    'varname': 'polityrelationshiptoprecedingentity', # key
    'col_exp': "The polity relationship to preceding (quasi)polity",
    'max_digits': 70,
    'choices': tuple_choices_maker_2(relationship_to_preceding_entity_CHOICES, "relationship_to_preceding_entity")[0],
    'null_meaning': "This polity did not have a relationship to preceding (quasi)polity"
    },
    {
    'colname': "preceding_entity",
    'dtype': MYTXT,
    'varname': 'polityprecedingentity', # key
    'col_exp': "The preceding entity or the largest settlement of a polity.",
    'max_digits': 70,
    'null_meaning': "This polity did not have a preceding entity."
    },
    {'colname': "succeeding_entity",
    'dtype': MYTXT,
    'varname': 'politysucceedingentity', # key
    'col_exp': "The succeeding entity or the largest settlement of a polity.",
    'max_digits': 70,
    'null_meaning': "This polity did not have a succeeding entity."
    },
    {
    'colname': "supracultural_entity",
    'dtype': MYTXT,
    'varname': 'politysupraculturalentity', # key
    'col_exp': "The supracultural entity or the largest settlement of a polity.",
    'max_digits': 100,
    'null_meaning': "This polity did not have a supracultural entity."
    },
    {
    'colname': "scale_from",
    'dtype': MYINT,
    'varname': 'scaleofsupraculturalinteraction', # key
    'col_exp': "The lower scale of supra cultural interactionfor a polity.",
    'units': "km squared",
    'min': 0,
    'null_meaning': "No_Value_Provided_in_Old_Wiki"
    },
    {
    'colname': "scale_to",
    'dtype': MYINT,
    'varname': 'scaleofsupraculturalinteraction', # key
    'col_exp':  "The upper scale of supra cultural interactionfor a polity.",
    'units': "km squared",
    'min': 0,
    'null_meaning': "No_Value_Provided_in_Old_Wiki"
    },
    {
    'colname': "alternate_religion_genus",
    'dtype': MYTXT_CH,
    'varname': 'polityalternatereligiongenus', # key
    'col_exp': "The alternate religion genus of a polity.",
    'max_digits': 70,
    'choices': tuple_choices_maker_2(religion_genus_CHOICES, "religion_genus")[0],
    'null_meaning': "This polity did not have a alternatereligion genus."
    },
    {
    'colname': "alternate_religion_family",
    'dtype': MYTXT_CH,
    'varname': 'polityalternatereligionfamily', # key
    'col_exp': "The alternate religion family of a polity.",
    'max_digits': 70,
    'choices': tuple_choices_maker_2(religion_family_CHOICES, "religion_family")[0],
    'null_meaning': "This polity did not have a alternate religion family."
    },
    {
    'colname': "alternate_religion",
    'dtype': MYTXT_CH,
    'varname': 'polityalternatereligion', # key
    'col_exp': "The alternate religion of a polity.",
    'max_digits': 70,
    'choices': tuple_choices_maker_2(religion_CHOICES, "religion")[0],
    'null_meaning': "This polity did not have a alternate religion ."
    },
    {
    'colname': "expert",
    'dtype': MYFOREIGN,
    'varname': 'polityexpert', # key
    'col_exp': "The expert of a polity.",
    'foreign_key': "SeshatExpert",
    'foreign_key_related_name': "seshat_expert",
    'null_meaning': "This polity did not have an expert."
    },
    {
    'colname': "editor",
    'dtype': MYFOREIGN,
    'varname': 'polityeditor', # key
    'col_exp': "The editor of a polity.",
    'foreign_key': "SeshatExpert",
    'foreign_key_related_name': "seshat_editor",
    'null_meaning': "This polity did not have an editor."
    },
    {
    'colname': "religious_tradition",
    'dtype': MYTXT,
    'varname': 'religioustradition', # key
    'col_exp': "The details of religious traditions.",
    'max_digits': 100,
    'null_meaning': "No_Value_Provided_in_Old_Wiki"
    }
]
