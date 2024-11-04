from otree.api import Currency as c, currency_range, safe_json
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player

class GenderAge(Page): #3
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['age', 'gender']

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

class Finance(Page): #3
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['rent', 'income']

class Postcode(Page):
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['postcode']

page_sequence = [GenderAge, Tutorials, LevelFamily, Finance, Postcode]
