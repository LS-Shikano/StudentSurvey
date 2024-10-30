from otree.api import Currency as c, currency_range, safe_json
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player
from . import *

class RandomNumber(Page): #16
    def vars_for_template(self):
        return {'rnumber': safe_json(self.player.rnumber),
                'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['rnumbercheck', 'time_rnumber']

class FirstEndPage(Page): #14
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['time_firstendpage']

class End(Page): #15
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['time_endpage']

page_sequence = [RandomNumber, FirstEndPage, End]
