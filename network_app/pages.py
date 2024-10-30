from otree.api import Currency as c, currency_range, safe_json
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player

class Participantcode(Page): #2
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['time_participantcode', 'participantcode']

class NetworkNamedPersons(Page): #4
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['person_1', 'person_2', 'person_3', 'person_4', 'person_5', 'person_6',
                   'person_7', 'person_8', 'person_9', 'person_10', 'person_11', 'person_12',
                   'person_13', 'person_14', 'person_15', 'person_16', 'person_17', 'person_18',
                   'person_19', 'person_20', 'person_21', 'person_22', 'person_23', 'person_24',
                   'person_25', 'person_26', 'person_27', 'person_28', 'person_29', 'person_30',
                   'person_31', 'person_32', 'person_33', 'person_34', 'person_35', 'person_36',
                   'person_37', 'person_38', 'person_39', 'person_40','time_networknamedstudents']

class NetworkFriendsPolitics(Page): #11
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['friends_1', 'friends_2', 'friends_3','friends_4','friends_5','friends_6','friends_7',
                   'friends_8','friends_9','friends_10','friends_11','friends_12','friends_13','friends_14',
                   'friends_15','friends_16','friends_17','friends_18','friends_19','friends_20','friends_21',
                   'friends_22','friends_23','friends_24','friends_25','friends_26','friends_27','friends_28',
                   'friends_29','friends_30','friends_31','friends_32','friends_33','friends_34','friends_35',
                   'friends_36','friends_37','friends_38','friends_39','friends_40',

                   'friends_politics_1', 'friends_politics_2', 'friends_politics_3','friends_politics_4','friends_politics_5','friends_politics_6','friends_politics_7',
                   'friends_politics_8','friends_politics_9','friends_politics_10','friends_politics_11','friends_politics_12','friends_politics_13','friends_politics_14',
                   'friends_politics_15','friends_politics_16','friends_politics_17','friends_politics_18','friends_politics_19','friends_politics_20','friends_politics_21',
                   'friends_politics_22','friends_politics_23','friends_politics_24','friends_politics_25','friends_politics_26','friends_politics_27','friends_politics_28',
                   'friends_politics_29','friends_politics_30','friends_politics_31','friends_politics_32','friends_politics_33','friends_politics_34','friends_politics_35',
                   'friends_politics_36','friends_politics_37','friends_politics_38','friends_politics_39','friends_politics_40', 'time_studentinteractions']

class NetworkFriends(Page): #12
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['time_studynetwork', 'learning_partner_1', 'learning_partner_2', 'learning_partner_3','learning_partner_4','learning_partner_5','learning_partner_6','learning_partner_7',
                   'learning_partner_8','learning_partner_9','learning_partner_10','learning_partner_11','learning_partner_12','learning_partner_13','learning_partner_14',
                   'learning_partner_15','learning_partner_16','learning_partner_17','learning_partner_18','learning_partner_19','learning_partner_20','learning_partner_21',
                   'learning_partner_22','learning_partner_23','learning_partner_24','learning_partner_25','learning_partner_26','learning_partner_27','learning_partner_28',
                   'learning_partner_29','learning_partner_30','learning_partner_31','learning_partner_32','learning_partner_33','learning_partner_34','learning_partner_35',
                   'learning_partner_36','learning_partner_37','learning_partner_38','learning_partner_39','learning_partner_40','learning_partner_41',

                   'network_student_council_1', 'network_student_council_2', 'network_student_council_3','network_student_council_4','network_student_council_5','network_student_council_6','network_student_council_7',
                   'network_student_council_8','network_student_council_9','network_student_council_10','network_student_council_11','network_student_council_12','network_student_council_13','network_student_council_14',
                   'network_student_council_15','network_student_council_16','network_student_council_17','network_student_council_18','network_student_council_19','network_student_council_20','network_student_council_21',
                   'network_student_council_22','network_student_council_23','network_student_council_24','network_student_council_25','network_student_council_26','network_student_council_27','network_student_council_28',
                   'network_student_council_29','network_student_council_30','network_student_council_31','network_student_council_32','network_student_council_33','network_student_council_34','network_student_council_35',
                   'network_student_council_36','network_student_council_37','network_student_council_38','network_student_council_39','network_student_council_40','network_student_council_41',
                   
                   'network_clubs_societies_1', 'network_clubs_societies_2', 'network_clubs_societies_3','network_clubs_societies_4','network_clubs_societies_5','network_clubs_societies_6','network_clubs_societies_7',
                   'network_clubs_societies_8','network_clubs_societies_9','network_clubs_societies_10','network_clubs_societies_11','network_clubs_societies_12','network_clubs_societies_13','network_clubs_societies_14',
                   'network_clubs_societies_15','network_clubs_societies_16','network_clubs_societies_17','network_clubs_societies_18','network_clubs_societies_19','network_clubs_societies_20','network_clubs_societies_21',
                   'network_clubs_societies_22','network_clubs_societies_23','network_clubs_societies_24','network_clubs_societies_25','network_clubs_societies_26','network_clubs_societies_27','network_clubs_societies_28',
                   'network_clubs_societies_29','network_clubs_societies_30','network_clubs_societies_31','network_clubs_societies_32','network_clubs_societies_33','network_clubs_societies_34','network_clubs_societies_35',
                   'network_clubs_societies_36','network_clubs_societies_37','network_clubs_societies_38','network_clubs_societies_39','network_clubs_societies_40','network_clubs_societies_41',
                   
                   'university_sport_network_1', 'university_sport_network_2', 'university_sport_network_3','university_sport_network_4','university_sport_network_5','university_sport_network_6','university_sport_network_7',
                   'university_sport_network_8','university_sport_network_9','university_sport_network_10','university_sport_network_11','university_sport_network_12','university_sport_network_13','university_sport_network_14',
                   'university_sport_network_15','university_sport_network_16','university_sport_network_17','university_sport_network_18','university_sport_network_19','university_sport_network_20','university_sport_network_21',
                   'university_sport_network_22','university_sport_network_23','university_sport_network_24','university_sport_network_25','university_sport_network_26','university_sport_network_27','university_sport_network_28',
                   'university_sport_network_29','university_sport_network_30','university_sport_network_31','university_sport_network_32','university_sport_network_33','university_sport_network_34','university_sport_network_35',
                   'university_sport_network_36','university_sport_network_37','university_sport_network_38','university_sport_network_39','university_sport_network_40','university_sport_network_41',
                  
                   'youth_party_network_1', 'youth_party_network_2', 'youth_party_network_3','youth_party_network_4','youth_party_network_5','youth_party_network_6','youth_party_network_7',
                   'youth_party_network_8','youth_party_network_9','youth_party_network_10','youth_party_network_11','youth_party_network_12','youth_party_network_13','youth_party_network_14',
                   'youth_party_network_15','youth_party_network_16','youth_party_network_17','youth_party_network_18','youth_party_network_19','youth_party_network_20','youth_party_network_21',
                   'youth_party_network_22','youth_party_network_23','youth_party_network_24','youth_party_network_25','youth_party_network_26','youth_party_network_27','youth_party_network_28',
                   'youth_party_network_29','youth_party_network_30','youth_party_network_31','youth_party_network_32','youth_party_network_33','youth_party_network_34','youth_party_network_35',
                   'youth_party_network_36','youth_party_network_37','youth_party_network_38','youth_party_network_39','youth_party_network_40','youth_party_network_41',  
                   
                   'value_opinion_1','value_opinion_2','value_opinion_3','value_opinion_4','value_opinion_5','value_opinion_6', 'value_opinion_7', 'value_opinion_8','value_opinion_9',
                   'value_opinion_10','value_opinion_11','value_opinion_12','value_opinion_13','value_opinion_14','value_opinion_15','value_opinion_16','value_opinion_17',
                   'value_opinion_18','value_opinion_19','value_opinion_20','value_opinion_21','value_opinion_22','value_opinion_23','value_opinion_24','value_opinion_25',
                   'value_opinion_26','value_opinion_27','value_opinion_28','value_opinion_29','value_opinion_30','value_opinion_31','value_opinion_32','value_opinion_33',
                   'value_opinion_34','value_opinion_35','value_opinion_36','value_opinion_37','value_opinion_38','value_opinion_39','value_opinion_40']

class LeftrightSelfassessment(Page): #8
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['linksrechts_self',                  
                   'linksrechts_1', 'linksrechts_2', 'linksrechts_3', 'linksrechts_4', 'linksrechts_5', 'linksrechts_6', 'linksrechts_7', 'linksrechts_8', 'linksrechts_9', 'linksrechts_10', 'linksrechts_11',
                   'linksrechts_12', 'linksrechts_13', 'linksrechts_14', 'linksrechts_15', 'linksrechts_16', 'linksrechts_17', 'linksrechts_18', 'linksrechts_19', 'linksrechts_20', 'linksrechts_21',
                   'linksrechts_22', 'linksrechts_23', 'linksrechts_24', 'linksrechts_25', 'linksrechts_26', 'linksrechts_27', 'linksrechts_28', 'linksrechts_29', 'linksrechts_30', 'linksrechts_31',
                   'linksrechts_32', 'linksrechts_33', 'linksrechts_34', 'linksrechts_35', 'linksrechts_36', 'linksrechts_37', 'linksrechts_38', 'linksrechts_39', 'linksrechts_40', 'time_leftright_selfassessment']


page_sequence = [Participantcode, NetworkNamedPersons, NetworkFriendsPolitics, NetworkFriends, LeftrightSelfassessment]
