MYINT = ['IntegerField', 'NumberInput']
MYDEC = ['DecimalField', 'NumberInput']
MYTXT = ['CharField', 'TextInput']
# for these we need, the pandas dfs to smartly select the choices, put them in a tuple or list
MYTXT_CH = ['CharField', 'Select']
MYFOREIGN = ['ForeignKey', 'Select']

# from all_choices import ALL_MY_CHOICES_GENERAL

sc_vars_dic_new = {'ra': {'varname': 'ra',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'The name of the research assistant or associate who coded the data. If more than one RA made a substantial contribution, list all via separate entries.',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'staff',
  'col1': {'colname': 'sc_ra',
   'dtype': ['ForeignKey', 'Select'],
   'varname': 'sc_research_assistant',
   'col_exp': 'The RA of Social Complexity Variables',
   'foreign_key': 'Seshat_Expert',
   'foreign_key_related_name': 'sc_research_assistant'}},
 'polity_territory': {'varname': 'polity_territory',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Social Scale, Polity territory is coded in squared kilometers.',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 2,
  'section': 'Social Complexity',
  'subsection': 'Social Scale',
  'col1': {'colname': 'polity_territory_from',
   'dtype': ['IntegerField', 'NumberInput'],
   'varname': 'polity_territory',
   'col_exp': 'The lower range of polity territory for a polity.',
   'max_digits': 20,
   'units': 'km squared'},
  'col2': {'colname': 'polity_territory_to',
   'dtype': ['IntegerField', 'NumberInput'],
   'varname': 'polity_territory',
   'col_exp': 'The lower range of polity territory for a polity.',
   'max_digits': 20,
   'units': 'km squared'}},
 'polity_population': {'varname': 'polity_population',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Social Scale, Polity Population is the estimated population of the polity; can change as a result of both adding/losing new territories or by population growth/decline within a region',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 2,
  'section': 'Social Complexity',
  'subsection': 'Social Scale',
  'col1': {'colname': 'polity_population_from',
   'dtype': ['IntegerField', 'NumberInput'],
   'varname': 'polity_population',
   'col_exp': 'The lower range of polity population for a polity.',
   'max_digits': 20},
  'col2': {'colname': 'polity_population_to',
   'dtype': ['IntegerField', 'NumberInput'],
   'varname': 'polity_population',
   'col_exp': 'The lower range of polity population for a polity.',
   'max_digits': 20}},
 'population_of_the_largest_settlement': {'varname': 'population_of_the_largest_settlement',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Social Scale, Population of the largest settlement is the estimated population of the largest settlement of the polity. Note that the largest settlement could be different from the capital (coded under General Variables). If possible, indicate the dynamics (that is, how population changed during the temporal period of the polity). Note that we are also building a city database - you should consult it as it may already have the needed data.',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 2,
  'section': 'Social Complexity',
  'subsection': 'Social Scale',
  'col1': {'colname': 'population_of_the_largest_settlement_from',
   'dtype': ['IntegerField', 'NumberInput'],
   'varname': 'population_of_the_largest_settlement',
   'col_exp': 'The lower range of population of the largest settlement for a polity.',
   'max_digits': 20},
  'col2': {'colname': 'population_of_the_largest_settlement_to',
   'dtype': ['IntegerField', 'NumberInput'],
   'varname': 'population_of_the_largest_settlement',
   'col_exp': 'The lower range of population of the largest settlement for a polity.',
   'max_digits': 20}},
 'settlement_hierarchy': {'varname': 'settlement_hierarchy',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Hierarchical Complexity, Settlement hierarchy records (in levels) the hierarchy of not just settlement sizes, but also their complexity as reflected in different roles they play within the (quasi)polity. As settlements become more populous they acquire more complex functions: transportational (e.g. port); economic (e.g. market); administrative (e.g. storehouse, local government building); cultural (e.g. theatre); religious (e.g. temple), utilitarian (e.g. hospital), monumental (e.g. statues, plazas). Example: (1) Large City (monumental structures, theatre, market, hospital, central government buildings) (2) City (market, theatre, regional government buildings) (3) Large Town (market, administrative buildings) (4) Town (administrative buildings, storehouse)) (5) Village (shrine) (6) Hamlet (residential only). In the narrative paragraph explain the different levels and list their functions. Provide a (crude) estimate of population sizes. For example, Large Town (market, temple, administrative buildings): 2,000-5,000 inhabitants.',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 2,
  'section': 'Social Complexity',
  'subsection': 'Hierarchical Complexity',
  'col1': {'colname': 'settlement_hierarchy_from',
   'dtype': ['IntegerField', 'NumberInput'],
   'varname': 'settlement_hierarchy',
   'col_exp': 'The lower range of settlement hierarchy for a polity.',
   'max_digits': 2,
   'min': 0},
  'col2': {'colname': 'settlement_hierarchy_to',
   'dtype': ['IntegerField', 'NumberInput'],
   'varname': 'settlement_hierarchy',
   'col_exp': 'The lower range of settlement hierarchy for a polity.',
   'max_digits': 2,
   'min': 0}},
 'administrative_level': {'varname': 'administrative_level',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': "Talking about Hierarchical Complexity, Administrative levels records the administrative levels of a polity. An example of hierarchy for a state society could be (1) the overall ruler, (2) provincial/regional governors, (3) district heads, (4) town mayors, (5) village heads. Note that unlike in settlement hierarchy, here you code people hierarchy. Do not simply copy settlement hierarchy data here. For archaeological polities, you will usually code as 'unknown', unless experts identified ranks of chiefs or officials independently of the settlement hierarchy. Note: Often there are more than one concurrent administrative hierarchy. In the example above the hierarchy refers to the territorial government. In addition, the ruler may have a hierarchically organized central bureaucracy located in the capital. For example, (4)the overall ruler, (3) chiefs of various ministries, (2) midlevel bureaucrats, (1) scribes and clerks. In the narrative paragraph detail what is known about both hierarchies. The machine-readable code should reflect the largest number (the longer chain of command).",
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 2,
  'section': 'Social Complexity',
  'subsection': 'Hierarchical Complexity',
  'col1': {'colname': 'administrative_level_from',
   'dtype': ['IntegerField', 'NumberInput'],
   'varname': 'administrative_level',
   'col_exp': 'The lower range of administrative level for a polity.',
   'max_digits': 2,
   'min': 0},
  'col2': {'colname': 'administrative_level_to',
   'dtype': ['IntegerField', 'NumberInput'],
   'varname': 'administrative_level',
   'col_exp': 'The lower range of administrative level for a polity.',
   'max_digits': 2,
   'min': 0}},
 'religious_level': {'varname': 'religious_level',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Hierarchical Complexity, Religious levels records the Religious levels of a polity. Same principle as with Administrative levels. Start with the head of the official cult (if present) coded as: level 1, and work down to the local priest.',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 2,
  'section': 'Social Complexity',
  'subsection': 'Hierarchical Complexity',
  'col1': {'colname': 'religious_level_from',
   'dtype': ['IntegerField', 'NumberInput'],
   'varname': 'religious_level',
   'col_exp': 'The lower range of religious level for a polity.',
   'max_digits': 2,
   'min': 0},
  'col2': {'colname': 'religious_level_to',
   'dtype': ['IntegerField', 'NumberInput'],
   'varname': 'religious_level',
   'col_exp': 'The lower range of religious level for a polity.',
   'max_digits': 2,
   'min': 0}},
 'military_level': {'varname': 'military_level',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Hierarchical Complexity, Military levels records the Military levels of a polity. Same principle as with Administrative levels. Start with the commander-in-chief coded as: level 1, and work down to the private. Even in primitive societies such as simple chiefdoms it is often possible to distinguish at least two levels – a commander and soldiers. A complex chiefdom would be coded three levels. The presence of warrior burials might be the basis for inferring the existence of a military organization. (The lowest military level is always the individual soldier).',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 2,
  'section': 'Social Complexity',
  'subsection': 'Hierarchical Complexity',
  'col1': {'colname': 'military_level_from',
   'dtype': ['IntegerField', 'NumberInput'],
   'varname': 'military_level',
   'col_exp': 'The lower range of military level for a polity.',
   'max_digits': 2,
   'min': 0},
  'col2': {'colname': 'military_level_to',
   'dtype': ['IntegerField', 'NumberInput'],
   'varname': 'military_level',
   'col_exp': 'The lower range of military level for a polity.',
   'max_digits': 2,
   'min': 0}},
 'professional_military_officer': {'varname': 'professional_military_officer',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Professions, Professional military officers refer to Full-time Professional military officers.',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Professions',
  'col1': {'colname': 'professional_military_officer',
   'dtype': ['CharField', 'Select'],
   'varname': 'professional_military_officer',
   'col_exp': 'The absence or presence of professional military officer for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'professional_soldier': {'varname': 'professional_soldier',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Professions, Professional soldiers refer to Full-time Professional soldiers.',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Professions',
  'col1': {'colname': 'professional_soldier',
   'dtype': ['CharField', 'Select'],
   'varname': 'professional_soldier',
   'col_exp': 'The absence or presence of professional soldier for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'professional_priesthood': {'varname': 'professional_priesthood',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Professions, Professional priesthood refers to Full-time Professional priesthood.',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Professions',
  'col1': {'colname': 'professional_priesthood',
   'dtype': ['CharField', 'Select'],
   'varname': 'professional_priesthood',
   'col_exp': 'The absence or presence of professional priesthood for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'full_time_bureaucrat': {'varname': 'full_time_bureaucrat',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': "Talking about Bureaucracy characteristics, Full-time bureaucrats refer to Full-time administrative specialists. Code this absent if administrative duties are performed by generalists such as chiefs and subchiefs. Also code it absent if state officials perform multiple functions, e.g. combining administrative tasks with military duties. Note that this variable shouldn't be coded 'present' only on the basis of the presence of specialized government buildings; there must be some additional evidence of functional specialization in government.",
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Bureaucracy characteristics',
  'col1': {'colname': 'full_time_bureaucrat',
   'dtype': ['CharField', 'Select'],
   'varname': 'full_time_bureaucrat',
   'col_exp': 'The absence or presence of full time bureaucrat for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'examination_system': {'varname': 'examination_system',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Bureaucracy characteristics, The paradigmatic example of an Examination system is the Chinese imperial system.',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Bureaucracy characteristics',
  'col1': {'colname': 'examination_system',
   'dtype': ['CharField', 'Select'],
   'varname': 'examination_system',
   'col_exp': 'The absence or presence of examination system for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'merit_promotion': {'varname': 'merit_promotion',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Bureaucracy characteristics, Merit promotion is coded present if there are regular, institutionalized procedures for promotion based on performance. When exceptional individuals are promoted to the top ranks, in the absence of institutionalized procedures, we code it under institution and equity variables',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Bureaucracy characteristics',
  'col1': {'colname': 'merit_promotion',
   'dtype': ['CharField', 'Select'],
   'varname': 'merit_promotion',
   'col_exp': 'The absence or presence of merit promotion for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'specialized_government_building': {'varname': 'specialized_government_building',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': "Talking about Bureaucracy characteristics, These buildings are where administrative officials are located, and must be distinct from the ruler's palace. They may be used for document storage, registration offices, minting money, etc. Defense structures also are not coded here (see Military). State-owned/operated workshop should also not be coded here.",
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Bureaucracy characteristics',
  'col1': {'colname': 'specialized_government_building',
   'dtype': ['CharField', 'Select'],
   'varname': 'specialized_government_building',
   'col_exp': 'The absence or presence of specialized government building for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'formal_legal_code': {'varname': 'formal_legal_code',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': "Talking about Law, Formal legal code refers to legal code usually, but not always written down. If not written down, code it 'present' when a uniform legal system is established by oral transmission (e.g., officials are taught the rules, or the laws are announced in a public space). Provide a short description",
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Law',
  'col1': {'colname': 'formal_legal_code',
   'dtype': ['CharField', 'Select'],
   'varname': 'formal_legal_code',
   'col_exp': 'The absence or presence of formal legal code for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'judge': {'varname': 'judge',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Law, judges refers only to full-time professional judges',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Law',
  'col1': {'colname': 'judge',
   'dtype': ['CharField', 'Select'],
   'varname': 'judge',
   'col_exp': 'The absence or presence of judge for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'court': {'varname': 'court',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Law, courts are buildings specialized for legal proceedings only.',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Law',
  'col1': {'colname': 'court',
   'dtype': ['CharField', 'Select'],
   'varname': 'court',
   'col_exp': 'The absence or presence of court for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'professional_lawyer': {'varname': 'professional_lawyer',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Law, NO_DESCRIPTIONS_IN_CODEBOOK.',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Law',
  'col1': {'colname': 'professional_lawyer',
   'dtype': ['CharField', 'Select'],
   'varname': 'professional_lawyer',
   'col_exp': 'The absence or presence of professional lawyer for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'irrigation_system': {'varname': 'irrigation_system',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Specialized Buildings, irrigation systems are polity owned (which includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Specialized Buildings',
  'col1': {'colname': 'irrigation_system',
   'dtype': ['CharField', 'Select'],
   'varname': 'irrigation_system',
   'col_exp': 'The absence or presence of irrigation system for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'drinking_water_supply_system': {'varname': 'drinking_water_supply_system',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Specialized Buildings, drinking water supply systems are polity owned (which includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Specialized Buildings',
  'col1': {'colname': 'drinking_water_supply_system',
   'dtype': ['CharField', 'Select'],
   'varname': 'drinking_water_supply_system',
   'col_exp': 'The absence or presence of drinking water supply system for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'market': {'varname': 'market',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Specialized Buildings, markets are polity owned (which includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Specialized Buildings',
  'col1': {'colname': 'market',
   'dtype': ['CharField', 'Select'],
   'varname': 'market',
   'col_exp': 'The absence or presence of market for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'food_storage_site': {'varname': 'food_storage_site',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Specialized Buildings, food storage sites are polity owned (which  includes owned by the community, or the state), NO_DESCRIPTIONS_IN_CODEBOOK',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Specialized Buildings',
  'col1': {'colname': 'food_storage_site',
   'dtype': ['CharField', 'Select'],
   'varname': 'food_storage_site',
   'col_exp': 'The absence or presence of food storage site for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'road': {'varname': 'road',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Transport infrastructure, roads refers to deliberately constructed roads that connect settlements or other sites. It excludes streets/accessways within settlements and paths between settlements that develop through repeated use.',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Transport infrastructure',
  'col1': {'colname': 'road',
   'dtype': ['CharField', 'Select'],
   'varname': 'road',
   'col_exp': 'The absence or presence of road for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'bridge': {'varname': 'bridge',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': "Talking about Transport infrastructure, bridges refers to bridges built and/or maintained by the polity (that is, code 'present' even if the polity did not build a bridge, but devotes resources to maintaining it).",
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Transport infrastructure',
  'col1': {'colname': 'bridge',
   'dtype': ['CharField', 'Select'],
   'varname': 'bridge',
   'col_exp': 'The absence or presence of bridge for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'canal': {'varname': 'canal',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': "Talking about Transport infrastructure, canals refers to canals built and/or maintained by the polity (that is, code 'present' even if the polity did not build a canal, but devotes resources to maintaining it).",
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Transport infrastructure',
  'col1': {'colname': 'canal',
   'dtype': ['CharField', 'Select'],
   'varname': 'canal',
   'col_exp': 'The absence or presence of canal for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'port': {'varname': 'port',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': "Talking about Transport infrastructure, Ports include river ports. Direct historical or archaeological evidence of Ports is absent when no port has been excavated or all evidence of such has been obliterated. Indirect historical or archaeological data is absent when there is no evidence that suggests that the polity engaged in maritime or riverine trade, conflict, or transportation, such as evidence of merchant shipping, administrative records of customs duties, or evidence that at the same period of time a trading relation in the region had a port (for example, due to natural processes, there is little evidence of ancient ports in delta Egypt at a time we know there was a timber trade with the Levant). When evidence for the variable itself is available the code is 'present.' When other forms of evidence suggests the existence of the variable (or not) the code may be 'inferred present' (or 'inferred absent'). When indirect evidence is not available the code will be either absent, temporal uncertainty, suspected unknown, or unknown.",
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Transport infrastructure',
  'col1': {'colname': 'port',
   'dtype': ['CharField', 'Select'],
   'varname': 'port',
   'col_exp': 'The absence or presence of port for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'mines_or_quarry': {'varname': 'mines_or_quarry',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Special purpose sites, NO_DESCRIPTIONS_IN_CODEBOOK',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Special purpose sites',
  'col1': {'colname': 'mines_or_quarry',
   'dtype': ['CharField', 'Select'],
   'varname': 'mines_or_quarry',
   'col_exp': 'The absence or presence of mines or quarry for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'mnemonic_device': {'varname': 'mnemonic_device',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Writing Systems, Mnemonic devices are: For example, tallies',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Writing Systems',
  'col1': {'colname': 'mnemonic_device',
   'dtype': ['CharField', 'Select'],
   'varname': 'mnemonic_device',
   'col_exp': 'The absence or presence of mnemonic device for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'nonwritten_record': {'varname': 'nonwritten_record',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': "Talking about Writing Systems, Nonwritten Records are more extensive than mnemonics, but don't utilize script. Example: quipu; seals and stamps",
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Writing Systems',
  'col1': {'colname': 'nonwritten_record',
   'dtype': ['CharField', 'Select'],
   'varname': 'nonwritten_record',
   'col_exp': 'The absence or presence of nonwritten record for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'written_record': {'varname': 'written_record',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Writing Systems, Written records are more than short and fragmentary inscriptions, such as found on tombs or runic stones. There must be several sentences strung together, at the very minimum. For example, royal proclamations from Mesopotamia and Egypt qualify as written records',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Writing Systems',
  'col1': {'colname': 'written_record',
   'dtype': ['CharField', 'Select'],
   'varname': 'written_record',
   'col_exp': 'The absence or presence of written record for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'script': {'varname': 'script',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Writing Systems, script is as indicated at least by fragmentary inscriptions (note that if written records are present, then so is script)',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Writing Systems',
  'col1': {'colname': 'script',
   'dtype': ['CharField', 'Select'],
   'varname': 'script',
   'col_exp': 'The absence or presence of script for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'non_phonetic_writing': {'varname': 'non_phonetic_writing',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Writing Systems, this refers to the kind of script',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Writing Systems',
  'col1': {'colname': 'non_phonetic_writing',
   'dtype': ['CharField', 'Select'],
   'varname': 'non_phonetic_writing',
   'col_exp': 'The absence or presence of non phonetic writing for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'phonetic_alphabetic_writing': {'varname': 'phonetic_alphabetic_writing',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Writing Systems, this refers to the kind of script',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Writing Systems',
  'col1': {'colname': 'phonetic_alphabetic_writing',
   'dtype': ['CharField', 'Select'],
   'varname': 'phonetic_alphabetic_writing',
   'col_exp': 'The absence or presence of phonetic alphabetic writing for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'lists_tables_and_classification': {'varname': 'lists_tables_and_classification',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Kinds of Written Documents',
  'col1': {'colname': 'lists_tables_and_classification',
   'dtype': ['CharField', 'Select'],
   'varname': 'lists_tables_and_classification',
   'col_exp': 'The absence or presence of lists tables and classification for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'calendar': {'varname': 'calendar',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Kinds of Written Documents',
  'col1': {'colname': 'calendar',
   'dtype': ['CharField', 'Select'],
   'varname': 'calendar',
   'col_exp': 'The absence or presence of calendar for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'sacred_text': {'varname': 'sacred_text',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Kinds of Written Documents, Sacred Texts originate from supernatural agents (deities), or are directly inspired by them.',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Kinds of Written Documents',
  'col1': {'colname': 'sacred_text',
   'dtype': ['CharField', 'Select'],
   'varname': 'sacred_text',
   'col_exp': 'The absence or presence of sacred text for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'religious_literature': {'varname': 'religious_literature',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Kinds of Written Documents, Religious literature differs from the sacred texts. For example, it may provide commentary on the sacred texts, or advice on how to live a virtuous life.',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Kinds of Written Documents',
  'col1': {'colname': 'religious_literature',
   'dtype': ['CharField', 'Select'],
   'varname': 'religious_literature',
   'col_exp': 'The absence or presence of religious literature for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'practical_literature': {'varname': 'practical_literature',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Kinds of Written Documents, Practical literature refers to texts written with the aim of providing guidance on a certain topic, for example manuals on agriculture, warfare, or cooking. Letters do not count as practical literature.',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Kinds of Written Documents',
  'col1': {'colname': 'practical_literature',
   'dtype': ['CharField', 'Select'],
   'varname': 'practical_literature',
   'col_exp': 'The absence or presence of practical literature for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'history': {'varname': 'history',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Kinds of Written Documents',
  'col1': {'colname': 'history',
   'dtype': ['CharField', 'Select'],
   'varname': 'history',
   'col_exp': 'The absence or presence of history for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'philosophy': {'varname': 'philosophy',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Kinds of Written Documents, NO_DESCRIPTIONS_IN_CODEBOOK',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Kinds of Written Documents',
  'col1': {'colname': 'philosophy',
   'dtype': ['CharField', 'Select'],
   'varname': 'philosophy',
   'col_exp': 'The absence or presence of philosophy for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'scientific_literature': {'varname': 'scientific_literature',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Kinds of Written Documents, Scientific literature includes mathematics, natural sciences, social sciences',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Kinds of Written Documents',
  'col1': {'colname': 'scientific_literature',
   'dtype': ['CharField', 'Select'],
   'varname': 'scientific_literature',
   'col_exp': 'The absence or presence of scientific literature for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'fiction': {'varname': 'fiction',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about Kinds of Written Documents, fiction includes poetry.',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Kinds of Written Documents',
  'col1': {'colname': 'fiction',
   'dtype': ['CharField', 'Select'],
   'varname': 'fiction',
   'col_exp': 'The absence or presence of fiction for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'article': {'varname': 'article',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about forms of money, articles are items that have both a regular use and are used as money (example: axes, cattle, measures of grain, ingots of non-precious metals)',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Forms of money',
  'col1': {'colname': 'article',
   'dtype': ['CharField', 'Select'],
   'varname': 'article',
   'col_exp': 'The absence or presence of article for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'token': {'varname': 'token',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about forms of money, tokens, unlike articles, are used only for exchange, and unlike coins, are not manufactured (example: cowries)',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Forms of money',
  'col1': {'colname': 'token',
   'dtype': ['CharField', 'Select'],
   'varname': 'token',
   'col_exp': 'The absence or presence of token for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'precious_metal': {'varname': 'precious_metal',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about forms of money, Precious metals are non-coined silver, gold, platinum',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Forms of money',
  'col1': {'colname': 'precious_metal',
   'dtype': ['CharField', 'Select'],
   'varname': 'precious_metal',
   'col_exp': 'The absence or presence of precious metal for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'foreign_coin': {'varname': 'foreign_coin',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'NO_DESCRIPTIONS_IN_CODEBOOK',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Forms of money',
  'col1': {'colname': 'foreign_coin',
   'dtype': ['CharField', 'Select'],
   'varname': 'foreign_coin',
   'col_exp': 'The absence or presence of foreign coin for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'indigenous_coin': {'varname': 'indigenous_coin',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'NO_DESCRIPTIONS_IN_CODEBOOK',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Forms of money',
  'col1': {'colname': 'indigenous_coin',
   'dtype': ['CharField', 'Select'],
   'varname': 'indigenous_coin',
   'col_exp': 'The absence or presence of indigenous coin for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'paper_currency': {'varname': 'paper_currency',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Paper currency or another kind of fiat money. Note that this only refers to indigenously produced paper currency. Code absent if colonial money is used.',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Forms of money',
  'col1': {'colname': 'paper_currency',
   'dtype': ['CharField', 'Select'],
   'varname': 'paper_currency',
   'col_exp': 'The absence or presence of paper currency for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'courier': {'varname': 'courier',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Full-time professional couriers.',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Postal sytems',
  'col1': {'colname': 'courier',
   'dtype': ['CharField', 'Select'],
   'varname': 'courier',
   'col_exp': 'The absence or presence of courier for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'postal_station': {'varname': 'postal_station',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': 'Talking about postal sytems, Postal stations are specialized buildings exclusively devoted to the postal service. If there is a special building that has other functions than a postal station, we still code postal station as present. The intent is to capture additional infrastructure beyond having a corps of messengers.',
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Postal sytems',
  'col1': {'colname': 'postal_station',
   'dtype': ['CharField', 'Select'],
   'varname': 'postal_station',
   'col_exp': 'The absence or presence of postal station for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}},
 'general_postal_service': {'varname': 'general_postal_service',
  'db_name': 'sc',
  'needsSeshatCommon': True,
  'main_desc': "Talking about postal sytems, 'General postal service' refers to a postal service that not only serves the ruler's needs, but carries mail for private citizens.",
  'main_desc_source': 'NOTHING',
  'notes': 'No_Actual_note',
  'cols': 1,
  'section': 'Social Complexity',
  'subsection': 'Postal sytems',
  'col1': {'colname': 'general_postal_service',
   'dtype': ['CharField', 'Select'],
   'varname': 'general_postal_service',
   'col_exp': 'The absence or presence of general postal service for a polity.',
   'choices': 'ABSENT_PRESENT_CHOICES'}}}