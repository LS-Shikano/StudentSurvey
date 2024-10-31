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
    rent = models.IntegerField(label="", initial="0")
    income = models.IntegerField(label="", initial="0")

    #lang = models.IntegerField() 
    edu_father = models.IntegerField(blank=True, max=4, min=-999, label="")
    edu_mother = models.IntegerField(blank=True, max=4, min=-999, label="")
    ocu_father = models.IntegerField(blank=True, max=1, min=-999, label="")
    ocu_mother = models.IntegerField(blank=True, max=1, min=-999, label="")

    ### Gender_age
    age = models.IntegerField(label="", initial="0")
    gender = models.IntegerField(blank=True, max=10, min=-999, label="")

    ### Tutorials
    tutorial = models.IntegerField(blank=True, max=8, min=-999, label="")
    grade = models.StringField(blank=True, label="")