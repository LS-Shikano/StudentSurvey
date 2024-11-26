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
    text_options_part7 = ['discriminated', 'sexually harassed']
    text_options_part8 = ['discriminatory gestures', 'harassment behavior']
    text_options_part9 = ['she', 'he']

class Subsession(BaseSubsession):
    def creating_session(self):
        
        for player in self.get_players():
            player.part1 = random.choice(Constants.text_options_part1)
            player.part2 = random.choice(Constants.text_options_part2)
            player.part3 = random.choice(Constants.text_options_part3)
            player.part4 = random.choice(Constants.text_options_part4)
            player.part5 = random.choice(Constants.text_options_part5)
            player.part6 = random.choice(Constants.text_options_part6)
            player.part7 = random.choice(Constants.text_options_part7)
            player.part8 = random.choice(Constants.text_options_part8)
            player.part9 = random.choice(Constants.text_options_part9)

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    harrassment = models.IntegerField(blank=True, max=5, min=-999, label="")
    part1 = models.StringField()  # Randomized part of the text
    part2 = models.StringField()
    part3 = models.StringField()  # Randomized part of the text
    part4 = models.StringField()
    part5 = models.StringField()  # Randomized part of the text
    part6 = models.StringField()
    part7 = models.StringField()  # Randomized part of the text
    part8 = models.StringField()  # Randomized part of the text
    part9 = models.StringField()  # Randomized part of the tex
