from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)
import random

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'vignett_app'
    players_per_group = None  # Set to None if not grouping players
    num_rounds = 1
    text_options_part1 = ['4-year-old child', '9-year-old child', '14-year-old teenager']  # Options for Part 1
    text_options_part2 = ['her', 'his']
    text_options_part3 = ['music', 'sport']
    text_options_part4 = ['kindergarten', 'school']
    text_options_part5 = ['study', 'experiment', 'simulation']
    text_options_part6 = ['study', 'experiment', 'simulation']  # Options for Part 2
    text_options_part7_mapped = {
        'showed a discriminatory note against': ['discriminated'],
        'committed a sexual harassment': ['sexually harassed']    }
    text_options_part8_mapped = {
        'discriminated': ['discriminatory gestures'],
        'sexually harassed': ['harassment behavior']    }
    text_options_part9 = ['she', 'he']
    text_options_part10 = ['showed a discriminatory note against', 'committed a sexual harassment']
    text_options_part11_mapped = {
        'showed a discriminatory note against' : ['Asian people', 'African people', 'South European people', 'Jewish people', 'Arab people'],
        'committed a sexual harassment': ['harassment behavior']    }

class Subsession(BaseSubsession):
    def creating_session(self):
        
        for player in self.get_players():
            player.part1 = random.choice(Constants.text_options_part1)
            player.part2 = random.choice(Constants.text_options_part2)
            player.part3 = random.choice(Constants.text_options_part3)
            player.part4 = random.choice(Constants.text_options_part4)
            player.part5 = random.choice(Constants.text_options_part5)
            player.part6 = random.choice(Constants.text_options_part6)
            player.part10 = random.choice(Constants.text_options_part10)
            player.part7 = random.choice(Constants.text_options_part7_mapped[player.part10])
            player.part8 = random.choice(Constants.text_options_part8_mapped[player.part7])
            player.part9 = random.choice(Constants.text_options_part9)
            player.part11 = random.choice(Constants.text_options_part11_mapped[player.part10])

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    harrassment = models.IntegerField(blank=True, max=5, min=-999, label="")
    part1 = models.StringField() 
    part2 = models.StringField()
    part3 = models.StringField()  
    part4 = models.StringField()
    part5 = models.StringField() 
    part6 = models.StringField()
    part10 = models.StringField()
    part7 = models.StringField()  
    part8 = models.StringField()  
    part9 = models.StringField()  
    part11 = models.StringField()
