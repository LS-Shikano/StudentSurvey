from otree.api import Currency as c, currency_range, safe_json
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player

class Sonntagsfrage(Page): #5
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['sunday_poll', 'sunday_party_vote', 'sunday_not_eligible', 'time_sundayquestion', 'noteligible_sunday_party_vote']

class ScaloParty(Page): #6
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['scalo_cdu', 'scalo_csu', 'scalo_spd', 'scalo_gruene', 'scalo_fdp', 'scalo_linke', 'scalo_afd', 'scalo_bsw', 'time_scaloparty']

class ScaloPerson(Page): #7
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['scalo_pep1', 'scalo_pep2', 'scalo_pep3', 'scalo_pep4', 'scalo_pep5', 'scalo_pep6', 'scalo_pep7', 'scalo_pep8',
                   'scalo_pep9', 'scalo_pep10', 'scalo_pep11', 'scalo_pep12', 'scalo_pep13', 'scalo_pep14', 'scalo_pep15','time_scaloperson']

class LeftRight(Page): #9
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['lr_CDU', 'lr_CSU', 'lr_SPD', 'lr_Gruene', 'lr_FDP', 'lr_Linke', 'lr_AfD', 'lr_BSW', 'time_leftright']

class PoliticalQuestions(Page): #10
    def vars_for_template(self):
        return {'lang': self.participant.vars.get('language')}
    form_model = Player
    form_fields = ['politics_question_one', 'politics_question_two', 'politics_question_three', 'politics_question_four',
                   'politics_question_five', 'politics_question_six', 'politics_question_seven','time_political_qs']

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

page_sequence = [Sonntagsfrage, ScaloParty, ScaloPerson, LeftRight, PoliticalQuestions, FirstEndPage, End]
