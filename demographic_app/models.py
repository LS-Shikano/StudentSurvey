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
    rent = models.IntegerField(blank=True, label="", min=0, max=10000)
    income = models.IntegerField(blank=True, label="", min=0, max=10000)

    #lang = models.IntegerField() 
    edu_father = models.IntegerField(blank=True, max=4, min=-999, label="")
    edu_mother = models.IntegerField(blank=True, max=4, min=-999, label="")
    ocu_father = models.IntegerField(blank=True, max=1, min=-999, label="")
    ocu_mother = models.IntegerField(blank=True, max=1, min=-999, label="")

    ### Gender_age
    age = models.IntegerField(blank=True, label="", min=10, max=100)
    gender = models.IntegerField(blank=True, max=10, min=-999, label="")

    study_program = models.IntegerField(blank=True, max=6, min=-999, label="")
    study_program_other = models.StringField(blank=True, label="")

    postcode = models.IntegerField(blank=True, label='', min=00, max=99)

    tutorial = models.IntegerField(blank=True, max=8, min=-999, label="")
    grade = models.StringField(blank=True, label="")

    social_networks_1 = models.IntegerField(blank=True, max=2, min=1, label="")
    social_networks_2 = models.IntegerField(blank=True, max=2, min=1, label="")
    social_networks_3 = models.IntegerField(blank=True, max=2, min=1, label="")
    social_networks_4 = models.IntegerField(blank=True, max=2, min=1, label="")
    social_networks_5 = models.IntegerField(blank=True, max=2, min=1, label="")
    social_networks_6 = models.IntegerField(blank=True, max=2, min=1, label="")
    social_networks_7 = models.IntegerField(blank=True, max=2, min=1, label="")
    social_networks_8 = models.IntegerField(blank=True, max=2, min=1, label="")
    social_networks_9 = models.IntegerField(blank=True, max=2, min=1, label="")
    social_networks_10 = models.IntegerField(blank=True, max=2, min=1, label="")
    social_networks_11 = models.StringField(blank=True, label="")

    participation_demonstration = models.IntegerField(blank=True, max=2, min=1, label="")
    participation_demonstration_1 = models.IntegerField(blank=True, max=2, min=1, label="")
    petition_signatory = models.IntegerField(blank=True, max=2, min=1, label="")
    petition_signatory_1 = models.IntegerField(blank=True, max=2, min=1, label = "")