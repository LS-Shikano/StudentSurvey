import random
#from . import constants

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
from conjoint.templates.conjoint.random_number import random_number

from conjoint.templates.conjoint.random_number import n_random_numbers, random_number


author = ''

doc = """
Your app description
"""


class Constants(BaseConstants):
    name_in_url = 'conjoint'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    def creating_session(self):
        for p in self.get_players():

            p.rnumber = random_number(100000, 999999)  # for the random number check

            random_numbers_vl = n_random_numbers(1, 3, 2)
            p.randomnumber_vl_1 = random_numbers_vl[0]
            p.randomnumber_vl_2 = random_numbers_vl[1]
            random_numbers_tut = n_random_numbers(1, 3, 2)
            p.randomnumber_tut_1 = random_numbers_tut[0]
            p.randomnumber_tut_2 = random_numbers_tut[1]
            random_numbers_ex = n_random_numbers(1, 3, 2)
            p.randomnumber_ex_1 = random_numbers_ex[0]
            p.randomnumber_ex_2 = random_numbers_ex[1]

            p.group_assignment = random_number(0,2) #used for randomization of the pictures

            random_numbers_questions = n_random_numbers(1, 14, 14)
            p.randomnumber_q1 = random_numbers_questions[0]
            p.randomnumber_q2 = random_numbers_questions[1]
            p.randomnumber_q3 = random_numbers_questions[2]
            p.randomnumber_q4 = random_numbers_questions[3]
            p.randomnumber_q5 = random_numbers_questions[4]
            p.randomnumber_q6 = random_numbers_questions[5]
            p.randomnumber_q7 = random_numbers_questions[6]
            p.randomnumber_q8 = random_numbers_questions[7]
            p.randomnumber_q9 = random_numbers_questions[8]
            p.randomnumber_q10 = random_numbers_questions[9]
            p.randomnumber_q11 = random_numbers_questions[10]
            p.randomnumber_q12 = random_numbers_questions[11]
            p.randomnumber_q13 = random_numbers_questions[12]
            p.randomnumber_q14 = random_numbers_questions[13]
            p.randomnumber_pop_2_2 = random_number(1, 2)
            p.randomnumber_pop_4_2 = random_number(1, 2)
            p.randomnumber_e_1_2 = random_number(1, 2)

            # input -999 for the cases in which the link is not shown in the condition
            if p.group_assignment == 0 or p.group_assignment == 2:
                p.link_check = '-999'


class Group(BaseGroup):
    def random_number(x, y):  # method for random integers
        rng = random.Random()
        number = rng.randint(x, y)
        return number

class Player(BasePlayer):
    # currently checking
    group_assignment = models.IntegerField()
    #link_check = models.StringField(blank=True)
    
    rnumber = models.IntegerField()

    ### Variable fuer Smartphone
    device_type = models.IntegerField()
    operating_system = models.IntegerField()
    browser = models.IntegerField()
    lang = models.IntegerField()

    ### Gender_age
    age = models.IntegerField(blank=True, max=6, min=1, label="")
    gender = models.IntegerField(blank=True, max=10, min=-999, label="")

    ### Participant Code
    participantcode = models.StringField(blank=False, label="")

    ### NetworkNamedPersons
    person_1 = models.StringField(blank=False, initial="[x]", label="")
    person_2 = models.StringField(blank=False, initial="[x]", label="")
    person_3 = models.StringField(blank=False, initial="[x]", label="")
    person_4 = models.StringField(blank=False, initial="[x]", label="")
    person_5 = models.StringField(blank=False, initial="[x]", label="")
    person_6 = models.StringField(blank=False, initial="[x]", label="")
    person_7 = models.StringField(blank=False, initial="[x]", label="")
    person_8 = models.StringField(blank=False, initial="[x]", label="")
    person_9 = models.StringField(blank=False, initial="[x]", label="")
    person_10 = models.StringField(blank=False, initial="[x]", label="")
    person_11 = models.StringField(blank=False, initial="[x]", label="")
    person_12 = models.StringField(blank=False, initial="[x]", label="")
    person_13 = models.StringField(blank=False, initial="[x]", label="")
    person_14 = models.StringField(blank=False, initial="[x]", label="")
    person_15 = models.StringField(blank=False, initial="[x]", label="")
    person_16 = models.StringField(blank=False, initial="[x]", label="")
    person_17 = models.StringField(blank=False, initial="[x]", label="")
    person_18 = models.StringField(blank=False, initial="[x]", label="")
    person_19 = models.StringField(blank=False, initial="[x]", label="")
    person_20 = models.StringField(blank=False, initial="[x]", label="")
    person_21 = models.StringField(blank=False, initial="[x]", label="")
    person_22 = models.StringField(blank=False, initial="[x]", label="")
    person_23 = models.StringField(blank=False, initial="[x]", label="")
    person_24 = models.StringField(blank=False, initial="[x]", label="")
    person_25 = models.StringField(blank=False, initial="[x]", label="")
    person_26 = models.StringField(blank=False, initial="[x]", label="")
    person_27 = models.StringField(blank=False, initial="[x]", label="")
    person_28 = models.StringField(blank=False, initial="[x]", label="")
    person_29 = models.StringField(blank=False, initial="[x]", label="")
    person_30 = models.StringField(blank=False, initial="[x]", label="")
    person_31 = models.StringField(blank=False, initial="[x]", label="")
    person_32 = models.StringField(blank=False, initial="[x]", label="")
    person_33 = models.StringField(blank=False, initial="[x]", label="")
    person_34 = models.StringField(blank=False, initial="[x]", label="")
    person_35 = models.StringField(blank=False, initial="[x]", label="")
    person_36 = models.StringField(blank=False, initial="[x]", label="")
    person_37 = models.StringField(blank=False, initial="[x]", label="")
    person_38 = models.StringField(blank=False, initial="[x]", label="")
    person_39 = models.StringField(blank=False, initial="[x]", label="")
    person_40 = models.StringField(blank=False, initial="[x]", label="")





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
    linksrechts_31 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_32 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_33 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_34 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_35 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_36 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_37 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_38 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_39 = models.IntegerField(blank=True, max=11, min=1, label="")
    linksrechts_40 = models.IntegerField(blank=True, max=11, min=1, label="")

    ### LeftRight

    


    ### PoliticalQuestions



    ### NetworkFriendsPolitics
    friends_1 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_2 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_3 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_4 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_5 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_6 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_7 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_8 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_9 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_10 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_11 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_12 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_13 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_14 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_15 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_16 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_17 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_18 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_19 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_20 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_21 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_22 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_23 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_24 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_25 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_26 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_27 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_28 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_29 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_30 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_31 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_32 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_33 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_34 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_35 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_36 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_37 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_38 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_39 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_40 = models.BooleanField(blank=True, max=2, min=1, label="")

    friends_politics_1 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_2 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_3 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_4 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_5 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_6 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_7 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_8 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_9 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_10 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_11 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_12 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_13 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_14 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_15 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_16 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_17 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_18 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_19 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_20 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_21 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_22 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_23 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_24 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_25 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_26 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_27 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_28 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_29 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_30 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_31 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_32 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_33 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_34 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_35 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_36 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_37 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_38 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_39 = models.BooleanField(blank=True, max=2, min=1, label="")
    friends_politics_40 = models.BooleanField(blank=True, max=2, min=1, label="")

    
    ### NetworkFriends

    learning_partner_1 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_2 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_3 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_4 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_5 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_6 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_7 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_8 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_9 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_10 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_11 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_12 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_13 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_14 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_15 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_16 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_17 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_18 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_19 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_20 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_21 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_22 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_23 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_24 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_25 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_26 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_27 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_28 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_29 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_30 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_31 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_32 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_33 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_34 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_35 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_36 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_37 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_38 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_39 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_40 = models.BooleanField(blank=True, max=2, min=1, label="")
    learning_partner_41 = models.BooleanField(blank=True, max=2, min=1, label="")


    network_student_council_1 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_2 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_3 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_4 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_5 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_6 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_7 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_8 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_9 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_10 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_11 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_12 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_13 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_14 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_15 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_16 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_17 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_18 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_19 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_20 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_21 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_22 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_23 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_24 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_25 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_26 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_27 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_28 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_29 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_30 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_31 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_32 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_33 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_34 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_35 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_36 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_37 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_38 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_39 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_40 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_student_council_41 = models.BooleanField(blank=True, max=2, min=1, label="")

    

    network_clubs_societies_1 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_2 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_3 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_4 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_5 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_6 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_7 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_8 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_9 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_10 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_11 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_12 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_13 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_14 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_15 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_16 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_17 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_18 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_19 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_20 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_21 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_22 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_23 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_24 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_25 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_26 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_27 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_28 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_29 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_30 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_31 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_32 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_33 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_34 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_35 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_36 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_37 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_38 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_39 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_40 = models.BooleanField(blank=True, max=2, min=1, label="")
    network_clubs_societies_41 = models.BooleanField(blank=True, max=2, min=1, label="")

    university_sport_network_1 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_2 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_3 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_4 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_5 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_6 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_7 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_8 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_9 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_10 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_11 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_12 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_13 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_14 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_15 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_16 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_17 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_18 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_19 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_20 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_21 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_22 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_23 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_24 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_25 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_26 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_27 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_28 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_29 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_30 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_31 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_32 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_33 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_34 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_35 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_36 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_37 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_38 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_39 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_40 = models.BooleanField(blank=True, max=2, min=1, label="")
    university_sport_network_41 = models.BooleanField(blank=True, max=2, min=1, label="")
    
    youth_party_network_1 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_2 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_3 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_4 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_5 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_6 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_7 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_8 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_9 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_10 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_11 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_12 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_13 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_14 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_15 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_16 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_17 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_18 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_19 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_20 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_21 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_22 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_23 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_24 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_25 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_26 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_27 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_28 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_29 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_30 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_31 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_32 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_33 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_34 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_35 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_36 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_37 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_38 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_39 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_40 = models.BooleanField(blank=True, max=2, min=1, label="")
    youth_party_network_41 = models.BooleanField(blank=True, max=2, min=1, label="")

    value_opinion_1 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_2 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_3 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_4 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_5 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_6 = models.BooleanField(blank=True, max=2, min=1, label="") 
    value_opinion_7 = models.BooleanField(blank=True, max=2, min=1, label="") 
    value_opinion_8 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_9 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_10 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_11 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_12 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_13 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_14 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_15 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_16 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_17 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_18 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_19 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_20 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_21 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_22 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_23 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_24 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_25 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_26 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_27 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_28 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_29 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_30 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_31 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_32 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_33 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_34 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_35 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_36 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_37 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_38 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_39 = models.BooleanField(blank=True, max=2, min=1, label="")
    value_opinion_40 = models.BooleanField(blank=True, max=2, min=1, label="")
    
    use_of_device = models.IntegerField(blank=True, max=3, min=1, label="")

    ### Tutorials
    tutorial = models.IntegerField(blank=True, max=10, min=1, label="")
    grade = models.StringField(blank=True, label="")

    ###RandomNumber
    ### zufällig generierte 6stellige Zufallszahl
    rnumbercheck = models.IntegerField(label="")
    def rnumbercheck_error_message(self, value):
        if value != self.rnumber:
            return "The confirmation number is wrong. Please try again!"



    ### Tutorials

    tutorial = models.IntegerField(blank=True, max=10, min=1, label="")
    grade = models.StringField(blank=True, label="")
    
   
    ### zufällig generierte 6stellige Zufallszahl
    rnumbercheck = models.IntegerField(label="")
    def rnumbercheck_error_message(self, value):
        if value != self.rnumber:
            return "The confirmation number is wrong. Please try again!"

    ### Time stamp variablen
    time_start = models.StringField(initial="-999")
    time_age = models.StringField(initial="-999")

    time_sundayquestion=models.StringField(initial="-999")
    time_scaloparty = models.StringField(initial="-999")
    time_scaloperson = models.StringField(initial="-999")

    time_leftright = models.StringField(initial="-999")
    time_pid = models.StringField(initial="-999")

    time_tutorial_expected_grade=models.StringField(initial="-999")

    time_rnumber= models.StringField(initial="-999")
    time_political_qs = models.StringField(initial="-999")

    time_networknamedstudents=models.StringField(initial="-999")
    time_leftright_selfassessment = models.StringField(initial="-999") 
    time_participantcode = models.StringField(initial="-999")
    time_fresherscamp=models.StringField(initial="-999")
    time_studynetwork=models.StringField(initial="-999")
    time_studentinteractions = models.StringField(initial="-999")





    ###Randomnumbers definition
    randomnumber_q1 = models.IntegerField()
    randomnumber_q2 = models.IntegerField()
    randomnumber_q3 = models.IntegerField()
    randomnumber_q4 = models.IntegerField()
    randomnumber_q5 = models.IntegerField()
    randomnumber_q6 = models.IntegerField()
    randomnumber_q7 = models.IntegerField()
    randomnumber_q8 = models.IntegerField()
    randomnumber_q9 = models.IntegerField()
    randomnumber_q10 = models.IntegerField()
    randomnumber_q11 = models.IntegerField()
    randomnumber_q12 = models.IntegerField()
    randomnumber_q13 = models.IntegerField()
    randomnumber_q14 =models.IntegerField()

    randomnumber_pop_2_2 = models.IntegerField()
    randomnumber_pop_4_2 = models.IntegerField()
    randomnumber_e_1_2 = models.IntegerField()
