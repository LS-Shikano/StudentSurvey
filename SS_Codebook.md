# Codebook Student Survey 

Codebook for the Student Survey

## Apps
- conjoint_app (CA)   
- demographic_app (DA)
- network_app (NA)
- political_app (PA)

## Survey Items  
Example: 
- Variable: `Name of the variable in code`
- Question: _Question answered by participants_
- Answers: _Possible options for answering the question_
- Page: _Part of the Otree survey that contains the item_

### CA - Conjoint App 

#### Time Started
- Variable: `time_start`
- Page: Welcome 

#### Language 
- Variable: `lang` 
- Page: Welcome

#### Type of Device
- Variable: `device_type`
- Page: Welcome

#### Type of OS
- Variable: `operating_system`
- Page: Welcome

#### Type of Browser
- Variable: `browser`
- Page: Welcome 

#### Random Number Generation 
- Variable: `rnumbercheck`
- Variable: `time_rnumber`
- Page: RandomNumber

***

### DA - Demographic App 

#### Age
- Variable: `age`
- Time answered: `time_age`
- Page: GenderAge
- Question: "Please enter your age in years."
- Answer: `Integer`

#### Gender 
- Variable: `gender`
- Page: GenderAge

#### Tutorial Participation 
- Variable: `tutorial`
- Page: Tutorials

#### Expected Grade 
- Variable: `grade`
- Variable: `time_tutorial_expected_grade`
- Page: Tutorials

***

### NA - Network App

#### Participant Code / Social-ID
- Variable: `time_participantcode`
- Variable: `participantcode`
- Page: 

#### Aquaintance Network
- Variable: [`person_1`:`person_40`]
- Variable: `time_networknamedstudents`
- Page: 

#### Friendship Network 
- Variable: [`friends_1`:`friends_40`]
- Page: 

#### Political Network 
- Variable: [`friends_politics_1`:`friends_politics_40`]
- Variable: `time_studentinteractions`
- Page: 

#### Study Network 
- Variable: [`learning_partner_1`:`learning_partner_41`]
- Variable: `time_studynetwork`

#### Student Council Network
- Variable: [`network_student_council_1`:`network_student_council_41`]


[`network_clubs_societies_1`:`network_clubs_societies_41`],
[`university_sport_network_1`:`university_sport_network_41`],
[`youth_party_network_1`:`youth_party_network_41`],
[`value_opinion_1`:`value_opinion_40`],

#### Political Identification for Self and Social Network 
- Variable: `linksrechts_self`
- Variable: [`linksrechts_1`:`linksrechts_40`]
- Variable: `time_leftright_selfassessment`
- Page: 

#### Kind of Device 
- Variable: `use_of_device`
- Page: 

***

### PA - Political App

`sunday_poll`, `sunday_party_vote`, `sunday_not_eligible`, `time_sundayquestion`, `noteligible_sunday_party_vote`

`scalo_cdu`, `scalo_csu`, `scalo_spd`, `scalo_gruene`, `scalo_fdp`, `scalo_linke`, `scalo_afd`, `scalo_bsw`, `time_scaloparty`

`scalo_pep1`, `scalo_pep2`, `scalo_pep3`, `scalo_pep4`, `scalo_pep5`, `scalo_pep6`, `scalo_pep7`, `scalo_pep8`,
`scalo_pep9`, `scalo_pep10`, `scalo_pep11`, `scalo_pep12`, `scalo_pep13`, `scalo_pep14`, `scalo_pep15`,`time_scaloperson`

`lr_CDU`, `lr_CSU`, `lr_SPD`, `lr_Gruene`, `lr_FDP`, `lr_Linke`, `lr_AfD`, `lr_BSW`, `time_leftright`

`politics_question_one`, `politics_question_two`, `politics_question_three`, `politics_question_four`,
`politics_question_five`, `politics_question_six`, `politics_question_seven`,`time_political_qs`

`time_firstendpage`

`time_endpage`