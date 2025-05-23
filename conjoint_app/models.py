

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

author = ''

doc = """
Your app description
"""

class Constants(BaseConstants):
    name_in_url = 'conjoint'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    device_type = models.IntegerField()
    operating_system = models.IntegerField()
    browser = models.IntegerField()
    time_start = models.StringField(initial="-999")

    lang = models.IntegerField()
    language = models.IntegerField() 
    use_of_device = models.IntegerField(blank=True, max=3, min=1, label="")
    participant_label = models.StringField()

