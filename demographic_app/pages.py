from otree.api import Currency as c, currency_range, safe_json
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player

class GenderAge(Page): #3
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['age', 'gender', 'study_program', 'study_program_other']

class Tutorials(Page): #13
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')} 
    form_model = Player
    form_fields = ['tutorial', 'grade']

class LevelFamily(Page): #3
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['edu_father', 'edu_mother', 'ocu_mother', 'ocu_father']

class Financial(Page): #3
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['rent', 'income']

class Postcode(Page):
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['postcode']

class Participation(Page):
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['participation_demonstration',
                   'participation_demonstration_1','petition_signatory','petition_signatory_1', 'social_networks_1','social_networks_2',
                   'social_networks_3','social_networks_4','social_networks_5','social_networks_6','social_networks_7','social_networks_8',
                   'social_networks_9', 'social_networks_10', 'social_networks_11']

page_sequence = [GenderAge, Tutorials, LevelFamily, Financial, Postcode, Participation]
