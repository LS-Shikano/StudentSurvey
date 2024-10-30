from otree.api import Currency as c, currency_range, safe_json
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player

class GenderAge(Page): #3
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['age', 'gender', 'time_age']

class Tutorials(Page): #13
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')} 
    form_model = Player
    form_fields = ['tutorial', 'grade', 'time_tutorial_expected_grade']


class edu_level_family(Page): #3
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['level_father', 'level_mother']

class finance(Page): #3
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['rent', 'income']

page_sequence = [GenderAge, Tutorials, edu_level_family, finance]
