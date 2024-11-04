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

    friend_2 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_2 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_2 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_2 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_2 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_3 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_3 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_3 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_3 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_3 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_4 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_4 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_4 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_4 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_4 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_5 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_5 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_5 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_5 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_5 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_6 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_6 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_6 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_6 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_6 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_7 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_7 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_7 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_7 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_7 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_8 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_8 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_8 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_8 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_8 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_9 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_9 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_9 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_9 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_9 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_10 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_10 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_10 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_10 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_10 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_11 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_11 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_11 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_11 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_11 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_12 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_12 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_12 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_12 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_12 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_13 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_13 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_13 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_13 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_13 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_14 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_14 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_14 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_14 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_14 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_15 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_15 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_15 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_15 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_15 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_16 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_16 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_16 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_16 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_16 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_17 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_17 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_17 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_17 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_17 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_18 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_18 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_18 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_18 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_18 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_19 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_19 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_19 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_19 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_19 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_20 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_20 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_20 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_20 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_20 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_21 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_21 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_21 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_21 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_21 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_22 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_22 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_22 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_22 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_22 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_23 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_23 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_23 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_23 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_23 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_24 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_24 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_24 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_24 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_24 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_25 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_25 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_25 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_25 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_25 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_26 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_26 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_26 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_26 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_26 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_27 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_27 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_27 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_27 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_27 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_28 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_28 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_28 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_28 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_28 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_29 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_29 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_29 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_29 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_29 = models.BooleanField(blank=True, max=2, min=1, label="")

    friend_30 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_30 = models.BooleanField(blank=True, max=2, min=1, label="")    
    politics_30 = models.BooleanField(blank=True, max=2, min=1, label="")
    study_30 = models.BooleanField(blank=True, max=2, min=1, label="") 
    council_30 = models.BooleanField(blank=True, max=2, min=1, label="")

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