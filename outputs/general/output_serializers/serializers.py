
################ Beginning of Serializers Imports (TODO: Make them automatic too)

from django.contrib.auth.models import User, Group
from rest_framework import serializers
from seshat.apps.general.models import Ra, Polity_territory, Polity_population, Population_of_the_largest_settlement, Settlement_hierarchy, Administrative_level, Religious_level, Military_level, Professional_military_officer, Professional_soldier, Professional_priesthood, Full_time_bureaucrat, Examination_system, Merit_promotion, Specialized_government_building, Formal_legal_code, Judge, Court, Professional_lawyer, Irrigation_system, Drinking_water_supply_system, Market, Food_storage_site, Road, Bridge, Canal, Port, Mines_or_quarry, Mnemonic_device, Nonwritten_record, Written_record, Script, Non_phonetic_writing, Phonetic_alphabetic_writing, Lists_tables_and_classification, Calendar, Sacred_text, Religious_literature, Practical_literature, History, Philosophy, Scientific_literature, Fiction, Article, Token, Precious_metal, Foreign_coin, Indigenous_coin, Paper_currency, Courier, Postal_station, General_postal_service
from ..core.models import Polity, Reference, Section, Subsection, Variablehierarchy

################ End of Serializers Imports

################ Beginning of Base Serializers
class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']

class ReferenceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reference
        fields = ['id', 'title', 'year', 'creator', 'zotero_link', 'long_name']
        
################ End of Base Serializers
################ Beginning of Serializers Imports

class RaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ra
        fields = ['year_from', 'year_to', 'sc_ra', 'tag']

class Polity_territorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_territory
        fields = ['year_from', 'year_to', 'polity_territory_from', 'polity_territory_to', 'tag']

class Polity_populationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Polity_population
        fields = ['year_from', 'year_to', 'polity_population_from', 'polity_population_to', 'tag']

class Population_of_the_largest_settlementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Population_of_the_largest_settlement
        fields = ['year_from', 'year_to', 'population_of_the_largest_settlement_from', 'population_of_the_largest_settlement_to', 'tag']

class Settlement_hierarchySerializer(serializers.ModelSerializer):
    class Meta:
        model = Settlement_hierarchy
        fields = ['year_from', 'year_to', 'settlement_hierarchy_from', 'settlement_hierarchy_to', 'tag']

class Administrative_levelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Administrative_level
        fields = ['year_from', 'year_to', 'administrative_level_from', 'administrative_level_to', 'tag']

class Religious_levelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Religious_level
        fields = ['year_from', 'year_to', 'religious_level_from', 'religious_level_to', 'tag']

class Military_levelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Military_level
        fields = ['year_from', 'year_to', 'military_level_from', 'military_level_to', 'tag']

class Professional_military_officerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional_military_officer
        fields = ['year_from', 'year_to', 'professional_military_officer', 'tag']

class Professional_soldierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional_soldier
        fields = ['year_from', 'year_to', 'professional_soldier', 'tag']

class Professional_priesthoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional_priesthood
        fields = ['year_from', 'year_to', 'professional_priesthood', 'tag']

class Full_time_bureaucratSerializer(serializers.ModelSerializer):
    class Meta:
        model = Full_time_bureaucrat
        fields = ['year_from', 'year_to', 'full_time_bureaucrat', 'tag']

class Examination_systemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Examination_system
        fields = ['year_from', 'year_to', 'examination_system', 'tag']

class Merit_promotionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Merit_promotion
        fields = ['year_from', 'year_to', 'merit_promotion', 'tag']

class Specialized_government_buildingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Specialized_government_building
        fields = ['year_from', 'year_to', 'specialized_government_building', 'tag']

class Formal_legal_codeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Formal_legal_code
        fields = ['year_from', 'year_to', 'formal_legal_code', 'tag']

class JudgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Judge
        fields = ['year_from', 'year_to', 'judge', 'tag']

class CourtSerializer(serializers.ModelSerializer):
    class Meta:
        model = Court
        fields = ['year_from', 'year_to', 'court', 'tag']

class Professional_lawyerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Professional_lawyer
        fields = ['year_from', 'year_to', 'professional_lawyer', 'tag']

class Irrigation_systemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Irrigation_system
        fields = ['year_from', 'year_to', 'irrigation_system', 'tag']

class Drinking_water_supply_systemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Drinking_water_supply_system
        fields = ['year_from', 'year_to', 'drinking_water_supply_system', 'tag']

class MarketSerializer(serializers.ModelSerializer):
    class Meta:
        model = Market
        fields = ['year_from', 'year_to', 'market', 'tag']

class Food_storage_siteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food_storage_site
        fields = ['year_from', 'year_to', 'food_storage_site', 'tag']

class RoadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Road
        fields = ['year_from', 'year_to', 'road', 'tag']

class BridgeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bridge
        fields = ['year_from', 'year_to', 'bridge', 'tag']

class CanalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Canal
        fields = ['year_from', 'year_to', 'canal', 'tag']

class PortSerializer(serializers.ModelSerializer):
    class Meta:
        model = Port
        fields = ['year_from', 'year_to', 'port', 'tag']

class Mines_or_quarrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Mines_or_quarry
        fields = ['year_from', 'year_to', 'mines_or_quarry', 'tag']

class Mnemonic_deviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mnemonic_device
        fields = ['year_from', 'year_to', 'mnemonic_device', 'tag']

class Nonwritten_recordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Nonwritten_record
        fields = ['year_from', 'year_to', 'nonwritten_record', 'tag']

class Written_recordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Written_record
        fields = ['year_from', 'year_to', 'written_record', 'tag']

class ScriptSerializer(serializers.ModelSerializer):
    class Meta:
        model = Script
        fields = ['year_from', 'year_to', 'script', 'tag']

class Non_phonetic_writingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Non_phonetic_writing
        fields = ['year_from', 'year_to', 'non_phonetic_writing', 'tag']

class Phonetic_alphabetic_writingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Phonetic_alphabetic_writing
        fields = ['year_from', 'year_to', 'phonetic_alphabetic_writing', 'tag']

class Lists_tables_and_classificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Lists_tables_and_classification
        fields = ['year_from', 'year_to', 'lists_tables_and_classification', 'tag']

class CalendarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Calendar
        fields = ['year_from', 'year_to', 'calendar', 'tag']

class Sacred_textSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sacred_text
        fields = ['year_from', 'year_to', 'sacred_text', 'tag']

class Religious_literatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Religious_literature
        fields = ['year_from', 'year_to', 'religious_literature', 'tag']

class Practical_literatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Practical_literature
        fields = ['year_from', 'year_to', 'practical_literature', 'tag']

class HistorySerializer(serializers.ModelSerializer):
    class Meta:
        model = History
        fields = ['year_from', 'year_to', 'history', 'tag']

class PhilosophySerializer(serializers.ModelSerializer):
    class Meta:
        model = Philosophy
        fields = ['year_from', 'year_to', 'philosophy', 'tag']

class Scientific_literatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scientific_literature
        fields = ['year_from', 'year_to', 'scientific_literature', 'tag']

class FictionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Fiction
        fields = ['year_from', 'year_to', 'fiction', 'tag']

class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ['year_from', 'year_to', 'article', 'tag']

class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = Token
        fields = ['year_from', 'year_to', 'token', 'tag']

class Precious_metalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Precious_metal
        fields = ['year_from', 'year_to', 'precious_metal', 'tag']

class Foreign_coinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foreign_coin
        fields = ['year_from', 'year_to', 'foreign_coin', 'tag']

class Indigenous_coinSerializer(serializers.ModelSerializer):
    class Meta:
        model = Indigenous_coin
        fields = ['year_from', 'year_to', 'indigenous_coin', 'tag']

class Paper_currencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Paper_currency
        fields = ['year_from', 'year_to', 'paper_currency', 'tag']

class CourierSerializer(serializers.ModelSerializer):
    class Meta:
        model = Courier
        fields = ['year_from', 'year_to', 'courier', 'tag']

class Postal_stationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Postal_station
        fields = ['year_from', 'year_to', 'postal_station', 'tag']

class General_postal_serviceSerializer(serializers.ModelSerializer):
    class Meta:
        model = General_postal_service
        fields = ['year_from', 'year_to', 'general_postal_service', 'tag']
class PolitySerializer(serializers.ModelSerializer):
	general_ra_related = RaSerializer(many=True, read_only=True)
	general_polity_territory_related = Polity_territorySerializer(many=True, read_only=True)
	general_polity_population_related = Polity_populationSerializer(many=True, read_only=True)
	general_population_of_the_largest_settlement_related = Population_of_the_largest_settlementSerializer(many=True, read_only=True)
	general_settlement_hierarchy_related = Settlement_hierarchySerializer(many=True, read_only=True)
	general_administrative_level_related = Administrative_levelSerializer(many=True, read_only=True)
	general_religious_level_related = Religious_levelSerializer(many=True, read_only=True)
	general_military_level_related = Military_levelSerializer(many=True, read_only=True)
	general_professional_military_officer_related = Professional_military_officerSerializer(many=True, read_only=True)
	general_professional_soldier_related = Professional_soldierSerializer(many=True, read_only=True)
	general_professional_priesthood_related = Professional_priesthoodSerializer(many=True, read_only=True)
	general_full_time_bureaucrat_related = Full_time_bureaucratSerializer(many=True, read_only=True)
	general_examination_system_related = Examination_systemSerializer(many=True, read_only=True)
	general_merit_promotion_related = Merit_promotionSerializer(many=True, read_only=True)
	general_specialized_government_building_related = Specialized_government_buildingSerializer(many=True, read_only=True)
	general_formal_legal_code_related = Formal_legal_codeSerializer(many=True, read_only=True)
	general_judge_related = JudgeSerializer(many=True, read_only=True)
	general_court_related = CourtSerializer(many=True, read_only=True)
	general_professional_lawyer_related = Professional_lawyerSerializer(many=True, read_only=True)
	general_irrigation_system_related = Irrigation_systemSerializer(many=True, read_only=True)
	general_drinking_water_supply_system_related = Drinking_water_supply_systemSerializer(many=True, read_only=True)
	general_market_related = MarketSerializer(many=True, read_only=True)
	general_food_storage_site_related = Food_storage_siteSerializer(many=True, read_only=True)
	general_road_related = RoadSerializer(many=True, read_only=True)
	general_bridge_related = BridgeSerializer(many=True, read_only=True)
	general_canal_related = CanalSerializer(many=True, read_only=True)
	general_port_related = PortSerializer(many=True, read_only=True)
	general_mines_or_quarry_related = Mines_or_quarrySerializer(many=True, read_only=True)
	general_mnemonic_device_related = Mnemonic_deviceSerializer(many=True, read_only=True)
	general_nonwritten_record_related = Nonwritten_recordSerializer(many=True, read_only=True)
	general_written_record_related = Written_recordSerializer(many=True, read_only=True)
	general_script_related = ScriptSerializer(many=True, read_only=True)
	general_non_phonetic_writing_related = Non_phonetic_writingSerializer(many=True, read_only=True)
	general_phonetic_alphabetic_writing_related = Phonetic_alphabetic_writingSerializer(many=True, read_only=True)
	general_lists_tables_and_classification_related = Lists_tables_and_classificationSerializer(many=True, read_only=True)
	general_calendar_related = CalendarSerializer(many=True, read_only=True)
	general_sacred_text_related = Sacred_textSerializer(many=True, read_only=True)
	general_religious_literature_related = Religious_literatureSerializer(many=True, read_only=True)
	general_practical_literature_related = Practical_literatureSerializer(many=True, read_only=True)
	general_history_related = HistorySerializer(many=True, read_only=True)
	general_philosophy_related = PhilosophySerializer(many=True, read_only=True)
	general_scientific_literature_related = Scientific_literatureSerializer(many=True, read_only=True)
	general_fiction_related = FictionSerializer(many=True, read_only=True)
	general_article_related = ArticleSerializer(many=True, read_only=True)
	general_token_related = TokenSerializer(many=True, read_only=True)
	general_precious_metal_related = Precious_metalSerializer(many=True, read_only=True)
	general_foreign_coin_related = Foreign_coinSerializer(many=True, read_only=True)
	general_indigenous_coin_related = Indigenous_coinSerializer(many=True, read_only=True)
	general_paper_currency_related = Paper_currencySerializer(many=True, read_only=True)
	general_courier_related = CourierSerializer(many=True, read_only=True)
	general_postal_station_related = Postal_stationSerializer(many=True, read_only=True)
	general_general_postal_service_related = General_postal_serviceSerializer(many=True, read_only=True)

	class Meta:
		model = Polity
		fields = ['id', 'name', 'start_year', 'end_year', 'general_ra_related', 'general_polity_territory_related', 'general_polity_population_related', 'general_population_of_the_largest_settlement_related', 'general_settlement_hierarchy_related', 'general_administrative_level_related', 'general_religious_level_related', 'general_military_level_related', 'general_professional_military_officer_related', 'general_professional_soldier_related', 'general_professional_priesthood_related', 'general_full_time_bureaucrat_related', 'general_examination_system_related', 'general_merit_promotion_related', 'general_specialized_government_building_related', 'general_formal_legal_code_related', 'general_judge_related', 'general_court_related', 'general_professional_lawyer_related', 'general_irrigation_system_related', 'general_drinking_water_supply_system_related', 'general_market_related', 'general_food_storage_site_related', 'general_road_related', 'general_bridge_related', 'general_canal_related', 'general_port_related', 'general_mines_or_quarry_related', 'general_mnemonic_device_related', 'general_nonwritten_record_related', 'general_written_record_related', 'general_script_related', 'general_non_phonetic_writing_related', 'general_phonetic_alphabetic_writing_related', 'general_lists_tables_and_classification_related', 'general_calendar_related', 'general_sacred_text_related', 'general_religious_literature_related', 'general_practical_literature_related', 'general_history_related', 'general_philosophy_related', 'general_scientific_literature_related', 'general_fiction_related', 'general_article_related', 'general_token_related', 'general_precious_metal_related', 'general_foreign_coin_related', 'general_indigenous_coin_related', 'general_paper_currency_related', 'general_courier_related', 'general_postal_station_related', 'general_general_postal_service_related']
    
################ End of Serializers Imports
