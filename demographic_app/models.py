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

doc = """
Your app description
"""

class Constants(BaseConstants):
    name_in_url = 'network'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    #lang = models.IntegerField() 

    ### Gender_age
    age = models.IntegerField(label="")
    gender = models.IntegerField(blank=True, max=10, min=-999, label="")
    time_age = models.StringField(initial="-999")

    ### Tutorials
    tutorial = models.IntegerField(blank=True, max=10, min=1, label="")
    grade = models.StringField(blank=True, label="")
    time_tutorial_expected_grade=models.StringField(initial="-999")