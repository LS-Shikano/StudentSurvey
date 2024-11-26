# ToDo

alten survey durchschauen wegen fragen die entfernt werden können 
    niedrige varianz
    niedrige response rate 

network among student + performance (build up this area)

konsolidierete version (testen mit AG)

liste mit random codes (3-stellige) manuell ausgegeben (Option!!!)
    hashfunktion mit matrikelnummer 
    personalisiert 

***

Three waves: Nomvember/ December/ January 

***

***
- [x] OTREE - Codebook befehl, automatisches (nicht mehr vorhanden-.-)
- [x] Zeitfrage - Anfang / Ende (Purged: conjoint, demographics) (entfernen kann sprachoptionen zerstören...)
- [x] Participationcode am Ende!!!!
- [x] SOCIAL-ID exchange is the first thing 
- [x] Tutoren liste CDM page (update)
- [x] Education + Job 
- [x] Rent (option living wioth parents)
- [x] Income (specify what exactly)
- [x] network items, delete placeholder, introduce big table for all relations 
- [x] clubs societies (remove)
- [x] sports (remove)
- [x] youth parties (remove)
- [x] PLZ - Herkunft des studis am anfang (First wave!)
- [x] Use of device - item to the beginning 
- [x] Update People in List of candidates (lang raus, biden raus, harris + netanjahu + zelenski added)
- [x] Problem mit doppelter Sprachanzeige (so halb gelöst... die alten dateien kopieren)
- [x] flexible amount of rows for network items!!!! (save variable of amount of people and access later on)
- [ ] final check of survey

***

## Feedback 

- [x] The left right ideology: We see different length of the scale for the self-placement and perception of others. Can we have the same length? You can put both in the same table. We also have to have "DK". (edited) 
    - DK??
- [x] I would ask differently. "Wie sehen Sie die folgenden Personen. Sie können mehr als eine Eigenschaft bei jeder Person angeben". or something like that. Response option should be correspondingly "Freund/in", "Ich schätze ihre/seine Meinung", "Ich diskutiere mit ihr/ihm über Politik", "Ich lerne zusammen", "Wir sind zusammen in der Fachschaft" or so. And the title "Spezielle Netzwerke" should be replaced by "Ihre Bekannten"
- [x] Actually the students' anonymous code consists of lower case letters or numbers.
- [x] Doing Left-Right Self-assessment and the one of the other people on the same page is prone to bias (in my opinion); instead of making a relatively independent assessment the individual compares themself with other people and that might influence the answers
- [x] There is no age cap for the age question; I entered 140 and there was no warning
- [x] Education Level Father - the text is really close to the bulletpoint; insert a space
- [x] I get the same error: 'Application error (500) TemplateLoadError: Loader cannot locate the template file 'demographic_app/Finance.html'.'
- [x] I got the same error at the end.
- [x] On the first page (“Willkommen & Welcome”) it first says “Ihre Teilnahme” but in the next sentence it says “ihr die Daten über euer…”. Maybe that should be consistent with the rest regarding how the respondents are adressed.
- [x] And I noticed some typos in the german version. For the “Selbsteinordnung” it says “Viel Leute” instead of “Viele Leute”. For the “Beschäftigung des Vaters” it says “Bitte geben Sie ob ihr Vater einer Beschäftigung nachgeht.”. And for the “Beschäftigung der Mutter” it says “Bitte geben Sie an ob ihr Vater einer Beschäftigung nachgeht”. And there is a parenthesis missing after Ph.D. for both

***

- xHere some further feedback. The anonymous code is here named "Sozial ID". This can be confusing. We should better not use such a term, but just name "Anonymous Code" or "Survey Code".
- We have three different sets of left-right questions. First, self-placement. Second, placement of alteri in respondents' networks. Third, political parties. Between the second and third, we have like-dislike of individual parties and politicians. This should be reversed so that subjects can answer the left-right questions in a block. We should not better make the survey unnecescessarilly challenging for respondents.
- xFor the rent (Miete) question, there is no upper limit. If you input a very large number, otree shows an error page subsequently. We should better set a realistic upper limit (e.g. 10T).

***

1. Sign up for an anonymous code by registering yourself on a sheet (matrikelnummer - survey code)
2. Exchange your code with other students whom you know 
3. take a memo for all information above. keep it until the end of the semester 

***
- Fixing the survey before analysing the first wave!
<<<<<<< HEAD
=======
	-x cant unselect relation in network item
	-x can not click "i dont know" for political parties 
	- Somehow make it work that codes are distributed by program (next year)
	- finance.html, leftrightSelfassesment (should change with deployed containers)
	- zurück button 
	- Question: Netzwerke der Messenger erstellen (whatsapp, signal, )
- Vignette App erstellen 
>>>>>>> 52568e226d8b5e1f550b1fa437ebfe9f37108d40
- Netzwerke erstellen 
	-x cant unselect relation in network item
	-x can not click "i dont know" for political parties 
	-x finance.html, leftrightSelfassesment (should change with deployed containers)
	-x zurück button (sehr aufwendig in Otree, sogar das beispiel nutzt ein einzelnes HTML dokument mit tabs)

- Question: Netzwerke der Messenger erstellen (whatsapp, signal, )
- Vignette App erstellen 

- Somehow make it work that codes are distributed by program (next year)