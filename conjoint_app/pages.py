from otree.api import Currency as c, currency_range, safe_json
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player
from . import *

class Welcome(Page): #1
    form_model = Player
    form_fields = ['lang', 'time_start', 'device_type', 'operating_system', 'browser', 'use_of_device']
    def before_next_page(self):
        self.participant.vars['language'] = self.player.lang

page_sequence = [Welcome] 
