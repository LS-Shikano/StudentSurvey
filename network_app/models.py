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
    name_in_url = 'network_app'
    players_per_group = None
    num_rounds = 1

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    ### Participant Code
    participantcode = models.StringField(blank=False, label="")
    def participantcode_error_message(self, value):
        # Check if the input is exactly 3 letters long and contains only alphabetic characters
        if len(value) != 3 or not value.isalpha() or not value.islower():
            return "Please enter exactly three lowercase letters."

    ### NetworkNamedPersons
    person_1 = models.StringField(blank=True, initial="x", label="")
    person_2 = models.StringField(blank=True, initial="x", label="")
    person_3 = models.StringField(blank=True, initial="x", label="")
    person_4 = models.StringField(blank=True, initial="x", label="")
    person_5 = models.StringField(blank=True, initial="x", label="")
    person_6 = models.StringField(blank=True, initial="x", label="")
    person_7 = models.StringField(blank=True, initial="x", label="")
    person_8 = models.StringField(blank=True, initial="x", label="")
    person_9 = models.StringField(blank=True, initial="x", label="")
    person_10 = models.StringField(blank=True, initial="x", label="")
    person_11 = models.StringField(blank=True, initial="x", label="")
    person_12 = models.StringField(blank=True, initial="x", label="")
    person_13 = models.StringField(blank=True, initial="x", label="")
    person_14 = models.StringField(blank=True, initial="x", label="")
    person_15 = models.StringField(blank=True, initial="x", label="")
    person_16 = models.StringField(blank=True, initial="x", label="")
    person_17 = models.StringField(blank=True, initial="x", label="")
    person_18 = models.StringField(blank=True, initial="x", label="")
    person_19 = models.StringField(blank=True, initial="x", label="")
    person_20 = models.StringField(blank=True, initial="x", label="")
    person_21 = models.StringField(blank=True, initial="x", label="")
    person_22 = models.StringField(blank=True, initial="x", label="")
    person_23 = models.StringField(blank=True, initial="x", label="")
    person_24 = models.StringField(blank=True, initial="x", label="")
    person_25 = models.StringField(blank=True, initial="x", label="")
    person_26 = models.StringField(blank=True, initial="x", label="")
    person_27 = models.StringField(blank=True, initial="x", label="")
    person_28 = models.StringField(blank=True, initial="x", label="")
    person_29 = models.StringField(blank=True, initial="x", label="")
    person_30 = models.StringField(blank=True, initial="x", label="")

    friend_1 = models.BooleanField(blank=True, initial=False)
    value_1 = models.BooleanField(blank=True, initial=False)    
    politics_1 = models.BooleanField(blank=True, initial=False)
    study_1 = models.BooleanField(blank=True, initial=False) 
    council_1 = models.BooleanField(blank=True, initial=False)

    friend_2 = models.BooleanField(blank=True, initial=False)
    value_2 = models.BooleanField(blank=True, initial=False)    
    politics_2 = models.BooleanField(blank=True, initial=False)
    study_2 = models.BooleanField(blank=True, initial=False) 
    council_2 = models.BooleanField(blank=True, initial=False)

    friend_3 = models.BooleanField(blank=True, initial=False)
    value_3 = models.BooleanField(blank=True, initial=False)    
    politics_3 = models.BooleanField(blank=True, initial=False)
    study_3 = models.BooleanField(blank=True, initial=False) 
    council_3 = models.BooleanField(blank=True, initial=False)

    friend_4 = models.BooleanField(blank=True, initial=False)
    value_4 = models.BooleanField(blank=True, initial=False)    
    politics_4 = models.BooleanField(blank=True, initial=False)
    study_4 = models.BooleanField(blank=True, initial=False) 
    council_4 = models.BooleanField(blank=True, initial=False)

    friend_5 = models.BooleanField(blank=True, initial=False)
    value_5 = models.BooleanField(blank=True, initial=False)    
    politics_5 = models.BooleanField(blank=True, initial=False)
    study_5 = models.BooleanField(blank=True, initial=False) 
    council_5 = models.BooleanField(blank=True, initial=False)

    friend_6 = models.BooleanField(blank=True, initial=False)
    value_6 = models.BooleanField(blank=True, initial=False)    
    politics_6 = models.BooleanField(blank=True, initial=False)
    study_6 = models.BooleanField(blank=True, initial=False) 
    council_6 = models.BooleanField(blank=True, initial=False)

    friend_7 = models.BooleanField(blank=True, initial=False)
    value_7 = models.BooleanField(blank=True, initial=False)    
    politics_7 = models.BooleanField(blank=True, initial=False)
    study_7 = models.BooleanField(blank=True, initial=False) 
    council_7 = models.BooleanField(blank=True, initial=False)

    friend_8 = models.BooleanField(blank=True, initial=False)
    value_8 = models.BooleanField(blank=True, initial=False)    
    politics_8 = models.BooleanField(blank=True, initial=False)
    study_8 = models.BooleanField(blank=True, initial=False) 
    council_8 = models.BooleanField(blank=True, initial=False)

    friend_9 = models.BooleanField(blank=True, initial=False)
    value_9 = models.BooleanField(blank=True, initial=False)    
    politics_9 = models.BooleanField(blank=True, initial=False)
    study_9 = models.BooleanField(blank=True, initial=False) 
    council_9 = models.BooleanField(blank=True, initial=False)

    friend_10 = models.BooleanField(blank=True, initial=False)
    value_10 = models.BooleanField(blank=True, initial=False)    
    politics_10 = models.BooleanField(blank=True, initial=False)
    study_10 = models.BooleanField(blank=True, initial=False) 
    council_10 = models.BooleanField(blank=True, initial=False)

    friend_11 = models.BooleanField(blank=True, initial=False)
    value_11 = models.BooleanField(blank=True, initial=False)    
    politics_11 = models.BooleanField(blank=True, initial=False)
    study_11 = models.BooleanField(blank=True, initial=False) 
    council_11 = models.BooleanField(blank=True, initial=False)

    friend_12 = models.BooleanField(blank=True, initial=False)
    value_12 = models.BooleanField(blank=True, initial=False)    
    politics_12 = models.BooleanField(blank=True, initial=False)
    study_12 = models.BooleanField(blank=True, initial=False) 
    council_12 = models.BooleanField(blank=True, initial=False)

    friend_13 = models.BooleanField(blank=True, initial=False)
    value_13 = models.BooleanField(blank=True, initial=False)    
    politics_13 = models.BooleanField(blank=True, initial=False)
    study_13 = models.BooleanField(blank=True, initial=False) 
    council_13 = models.BooleanField(blank=True, initial=False)

    friend_14 = models.BooleanField(blank=True, initial=False)
    value_14 = models.BooleanField(blank=True, initial=False)    
    politics_14 = models.BooleanField(blank=True, initial=False)
    study_14 = models.BooleanField(blank=True, initial=False) 
    council_14 = models.BooleanField(blank=True, initial=False)

    friend_15 = models.BooleanField(blank=True, initial=False)
    value_15 = models.BooleanField(blank=True, initial=False)    
    politics_15 = models.BooleanField(blank=True, initial=False)
    study_15 = models.BooleanField(blank=True, initial=False) 
    council_15 = models.BooleanField(blank=True, initial=False)

    friend_16 = models.BooleanField(blank=True, initial=False)
    value_16 = models.BooleanField(blank=True, initial=False)    
    politics_16 = models.BooleanField(blank=True, initial=False)
    study_16 = models.BooleanField(blank=True, initial=False) 
    council_16 = models.BooleanField(blank=True, initial=False)

    friend_17 = models.BooleanField(blank=True, initial=False)
    value_17 = models.BooleanField(blank=True, initial=False)    
    politics_17 = models.BooleanField(blank=True, initial=False)
    study_17 = models.BooleanField(blank=True, initial=False) 
    council_17 = models.BooleanField(blank=True, initial=False)

    friend_18 = models.BooleanField(blank=True, initial=False)
    value_18 = models.BooleanField(blank=True, initial=False)    
    politics_18 = models.BooleanField(blank=True, initial=False)
    study_18 = models.BooleanField(blank=True, initial=False) 
    council_18 = models.BooleanField(blank=True, initial=False)

    friend_19 = models.BooleanField(blank=True, initial=False)
    value_19 = models.BooleanField(blank=True, initial=False)    
    politics_19 = models.BooleanField(blank=True, initial=False)
    study_19 = models.BooleanField(blank=True, initial=False) 
    council_19 = models.BooleanField(blank=True, initial=False)

    friend_20 = models.BooleanField(blank=True, initial=False)
    value_20 = models.BooleanField(blank=True, initial=False)    
    politics_20 = models.BooleanField(blank=True, initial=False)
    study_20 = models.BooleanField(blank=True, initial=False) 
    council_20 = models.BooleanField(blank=True, initial=False)

    friend_21 = models.BooleanField(blank=True, initial=False)
    value_21 = models.BooleanField(blank=True, initial=False)    
    politics_21 = models.BooleanField(blank=True, initial=False)
    study_21 = models.BooleanField(blank=True, initial=False) 
    council_21 = models.BooleanField(blank=True, initial=False)

    friend_22 = models.BooleanField(blank=True, initial=False)
    value_22 = models.BooleanField(blank=True, initial=False)    
    politics_22 = models.BooleanField(blank=True, initial=False)
    study_22 = models.BooleanField(blank=True, initial=False) 
    council_22 = models.BooleanField(blank=True, initial=False)

    friend_23 = models.BooleanField(blank=True, initial=False)
    value_23 = models.BooleanField(blank=True, initial=False)    
    politics_23 = models.BooleanField(blank=True, initial=False)
    study_23 = models.BooleanField(blank=True, initial=False) 
    council_23 = models.BooleanField(blank=True, initial=False)

    friend_24 = models.BooleanField(blank=True, initial=False)
    value_24 = models.BooleanField(blank=True, initial=False)    
    politics_24 = models.BooleanField(blank=True, initial=False)
    study_24 = models.BooleanField(blank=True, initial=False) 
    council_24 = models.BooleanField(blank=True, initial=False)

    friend_25 = models.BooleanField(blank=True, initial=False)
    value_25 = models.BooleanField(blank=True, initial=False)    
    politics_25 = models.BooleanField(blank=True, initial=False)
    study_25 = models.BooleanField(blank=True, initial=False) 
    council_25 = models.BooleanField(blank=True, initial=False)

    friend_26 = models.BooleanField(blank=True, initial=False)
    value_26 = models.BooleanField(blank=True, initial=False)    
    politics_26 = models.BooleanField(blank=True, initial=False)
    study_26 = models.BooleanField(blank=True, initial=False) 
    council_26 = models.BooleanField(blank=True, initial=False)

    friend_27 = models.BooleanField(blank=True, initial=False)
    value_27 = models.BooleanField(blank=True, initial=False)    
    politics_27 = models.BooleanField(blank=True, initial=False)
    study_27 = models.BooleanField(blank=True, initial=False) 
    council_27 = models.BooleanField(blank=True, initial=False)

    friend_28 = models.BooleanField(blank=True, initial=False)
    value_28 = models.BooleanField(blank=True, initial=False)    
    politics_28 = models.BooleanField(blank=True, initial=False)
    study_28 = models.BooleanField(blank=True, initial=False) 
    council_28 = models.BooleanField(blank=True, initial=False)

    friend_29 = models.BooleanField(blank=True, initial=False)
    value_29 = models.BooleanField(blank=True, initial=False)    
    politics_29 = models.BooleanField(blank=True, initial=False)
    study_29 = models.BooleanField(blank=True, initial=False) 
    council_29 = models.BooleanField(blank=True, initial=False)

    friend_30 = models.BooleanField(blank=True, initial=False)
    value_30 = models.BooleanField(blank=True, initial=False)    
    politics_30 = models.BooleanField(blank=True, initial=False)
    study_30 = models.BooleanField(blank=True, initial=False) 
    council_30 = models.BooleanField(blank=True, initial=False)

    ### LeftrightSelfassessment
    linksrechts_self = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_1 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_2 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_3 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_4 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_5 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_6 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_7 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_8 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_9 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_10 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_11 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_12 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_13 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_14 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_15 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_16 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_17 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_18 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_19 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_20 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_21 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_22 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_23 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_24 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0) 
    linksrechts_25 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_26 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_27 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_28 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_29 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)
    linksrechts_30 = models.IntegerField(blank=True, max=11, min=1, label="", initial=0)