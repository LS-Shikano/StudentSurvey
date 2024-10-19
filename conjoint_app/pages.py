from otree.api import Currency as c, currency_range, safe_json
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player
from . import *

class Welcome(Page): #1
    form_model = Player
    form_fields = ['lang', 'time_start', 'device_type', 'operating_system', 'browser']
    
    def before_next_page(self):
        self.participant.vars['language'] = self.player.lang

class RandomNumber(Page): #16
    def vars_for_template(self):
        return {'rnumber': safe_json(self.player.rnumber),
                'lang': self.player.lang}
    form_model = Player
    form_fields = ['rnumbercheck', 'time_rnumber']

page_sequence = [Welcome, RandomNumber] 
