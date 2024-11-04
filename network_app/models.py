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
    person_1 = models.StringField(blank=False, initial="x", label="")
    person_2 = models.StringField(blank=False, initial="x", label="")
    person_3 = models.StringField(blank=False, initial="x", label="")
    person_4 = models.StringField(blank=False, initial="x", label="")
    person_5 = models.StringField(blank=False, initial="x", label="")
    person_6 = models.StringField(blank=False, initial="x", label="")
    person_7 = models.StringField(blank=False, initial="x", label="")
    person_8 = models.StringField(blank=False, initial="x", label="")
    person_9 = models.StringField(blank=False, initial="x", label="")
    person_10 = models.StringField(blank=False, initial="x", label="")
    person_11 = models.StringField(blank=False, initial="x", label="")
    person_12 = models.StringField(blank=False, initial="x", label="")
    person_13 = models.StringField(blank=False, initial="x", label="")
    person_14 = models.StringField(blank=False, initial="x", label="")
    person_15 = models.StringField(blank=False, initial="x", label="")
    person_16 = models.StringField(blank=False, initial="x", label="")
    person_17 = models.StringField(blank=False, initial="x", label="")
    person_18 = models.StringField(blank=False, initial="x", label="")
    person_19 = models.StringField(blank=False, initial="x", label="")
    person_20 = models.StringField(blank=False, initial="x", label="")
    person_21 = models.StringField(blank=False, initial="x", label="")
    person_22 = models.StringField(blank=False, initial="x", label="")
    person_23 = models.StringField(blank=False, initial="x", label="")
    person_24 = models.StringField(blank=False, initial="x", label="")
    person_25 = models.StringField(blank=False, initial="x", label="")
    person_26 = models.StringField(blank=False, initial="x", label="")
    person_27 = models.StringField(blank=False, initial="x", label="")
    person_28 = models.StringField(blank=False, initial="x", label="")
    person_29 = models.StringField(blank=False, initial="x", label="")
    person_30 = models.StringField(blank=False, initial="x", label="")

    friend_1 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_1 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_1 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_1 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_1 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_2 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_2 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_2 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_2 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_2 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_3 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_3 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_3 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_3 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_3 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_4 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_4 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_4 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_4 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_4 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_5 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_5 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_5 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_5 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_5 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_6 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_6 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_6 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_6 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_6 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_7 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_7 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_7 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_7 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_7 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_8 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_8 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_8 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_8 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_8 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_9 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_9 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_9 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_9 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_9 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_10 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_10 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_10 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_10 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_10 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_11 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_11 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_11 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_11 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_11 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_12 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_12 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_12 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_12 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_12 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_13 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_13 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_13 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_13 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_13 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_14 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_14 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_14 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_14 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_14 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_15 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_15 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_15 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_15 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_15 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_16 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_16 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_16 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_16 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_16 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_17 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_17 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_17 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_17 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_17 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_18 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_18 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_18 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_18 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_18 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_19 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_19 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_19 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_19 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_19 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_20 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_20 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_20 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_20 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_20 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_21 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_21 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_21 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_21 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_21 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_22 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_22 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_22 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_22 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_22 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_23 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_23 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_23 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_23 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_23 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_24 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_24 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_24 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_24 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_24 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_25 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_25 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_25 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_25 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_25 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_26 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_26 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_26 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_26 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_26 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_27 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_27 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_27 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_27 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_27 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_28 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_28 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_28 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_28 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_28 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_29 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_29 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_29 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_29 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_29 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    friend_30 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    value_30 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)    
    politics_30 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)
    study_30 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0) 
    council_30 = models.BooleanField(blank=True, max=2, min=1, label="", initial=0)

    ### LeftrightSelfassessment
    linksrechts_self = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_1 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_2 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_3 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_4 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_5 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_6 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_7 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_8 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_9 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_10 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_11 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_12 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_13 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_14 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_15 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_16 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_17 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_18 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_19 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_20 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_21 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_22 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_23 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_24 = models.IntegerField(blank=True, max=11, min=1, label="") 
    linksrechts_25 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_26 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_27 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_28 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_29 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_30 = models.IntegerField(blank=True, max=11, min=1, label="")