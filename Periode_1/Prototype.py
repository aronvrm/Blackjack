"""
Dit prototype is bedoeld om de gebruiker te informeren en activeren voor crowd logistics.
Op basis van hero's journey is een verhaal geschreven om de gebruiker mee te nemen in een verhaallijn rondom crowd logistics.
Hoe het verhaal loopt is afhankelijk van de keuze van de gebruiker.
"""

from itertools import chain
import time
from time import sleep
import webbrowser

# typewriter effect
KPS = 15  # Aantal karakters per seconden

# Dit effect zorgt ervoor dat er een typewriter effect ontstaat


def type(text, delay=1/KPS):  # text en berekening van de snelheid
    for line in text.splitlines():  # for loop om nieuwe strings te splitten
        interval = len(line)+1  # interval define
        print('')  # print statement
        for i in chain(range(interval)):  # nieuwe for loop voor toepassing functie
            print('\r' + line[:i], end="")  # print en slicing van de functie
            sleep(delay)  # toepassing van de snelheid


# Keuze om pakketje te bezorgen of niet. (Beloning)


def beloning_functie():

    beloning_keuze = input(
        "\nNu is de vraag, ga jij het pakketje bezorgen? (kies ja of nee) ").lower()
    if beloning_keuze == "ja":
        beloning_2()

    elif beloning_keuze == "nee":
        einde_eerder()

    else:
        type("dat is geen geldige keuze! je moet ja of nee kiezen")
        beloning_keuze

# Keuze om het pakketje te bezorgen of niet. (Intrinsiek)


def intris_functie():

    intrisieke_keuze = input(
        "\nNu is de vraag, ga jij het pakketje bezorgen? (kies ja of nee) ").lower()
    if intrisieke_keuze == "ja":
        intrisieke_vervolg()

    elif intrisieke_keuze == "nee":
        einde_eerder()

    else:
        type("dat is geen geldige keuze! je moet ja of nee kiezen")
        intrisieke_keuze


# Vragen om naam
type("Welkom wereldveranderaar!")
username = input("\nWat is je naam? ")

# Opening van het verhaal
print("Hoi", username, "leuk dat je deelneemt aan dit duurzame avontuur!")
type("Het is de 21e eeuw. De wereld bevindt zich momenteel in een klimaatcrisis.")
type("In dit verhaal gaan we je meenemen in een duurzaam alternatief voor jou pakketje.")
type("Namelijk crowd logistics! ")
type("Als jij deelneemt aan crowd logistics ga jij een pakketje bezorgen terwijl je al onderweg bent.")
type("En dat zonder veel extra om te hoeven rijden.")
type("Op deze manier hoeven er minder pakketbusjes te rijden, wat beter is voor de doorstroming en het mileu.")
type("\nNu zijn wij heel benieuwd!")

keuze_intrinsiek_of_beloning = True

# ________________________________________________________


# Hier ga je verder als je het op basis van intrinsieke motivatie al zou doen!
def intrinsiek():
    type("Je scrolt over je Facebook tijdlijn en je ziet een advertentie voorbijkomen van Crowd to door.")
    type("Crowd to door is een online crowd logistics platform.")
    type("Je ziet dat jij je steentje kan bijdragen aan duurzame alternatieven.")
    type("door pakketjes af te leveren bij mensen als je toch al onderweg bent.")
    type("Binnen 2 dagen krijg je een oproep om een pakketje af te leveren als je uit je werk komt.")
    type("Hiervoor ben je 20 minuten langer onderweg.")
    type("Je hebt in de middagpauze met je collega's over het pakketje dat je kan bezorgen.")
    type("2 collega's zijn super enthousiast.")
    type("Ze vinden het goed van je dat jij je steentje bijdraagt aan een duurzamere samenleving.")
    type("Een andere collega vindt het zeer nutteloos.")
    type("Je krijgt opmerkingen naar je hoofd zoals, daar heb je toch pakketbedrijven voor!")
    type("Je pauze is net voorbij en je krijgt de melding dat je binnen een uur moet beslissen of je het pakket gaat bezorgen. ")
    intris_functie()


def intrisieke_vervolg():
    type("Na je werk stap je in de auto en rij je langs de locatie waar je pakketje ophaalt. ")
    type("Deze locatie ligt op jou route naar huis. ")
    type("Vervolgens rij je een klein stukje om, om het pakketje langs te brengen. ")
    type("Je stapt uit, belt aan. En een hele aardige vrouw doet open. ")
    type("Ze is zo enthousiast dat je mee doet aan crowd logistics. Ze is je heel dankbaar. ")
    type("Twee dagen later krijg je opnieuw een melding van Crowd to Door of je een pakketje wil bezorgen. ")
    type("Hiervoor moet je een kwartiertje omrijden op de fiets als je naar de voetbaltraining toegaat. ")
    type("Het is maar een klein pakketje. ")
    type("Je moet 15 minuten omfietsen. ")


# Dit was het verhaal op basis van intrinsieke motivatie
# ________________________________________________________


# Hier ga je verder als je een beloning nodig hebt
def beloning():
    type("Je scrolt over je Facebook tijdlijn en je ziet een advertentie voorbijkomen van Crowd to door.")
    type("Crowd to door is een online crowd logistics platform.")
    type("Je ziet dat je lekker kan bijverdienen door pakketjes af te leveren bij mensen als je toch al onderweg bent.")
    type("Dit is een leuke bijverdienste en je schrijft je dus in!")
    type("Binnen 2 dagen krijg je een oproep om een pakketje af te leveren als je uit je werk komt.")
    type("Hiervoor ben je 20 minuten langer onderweg en levert het je 10 euro op.")
    type("Je hebt in de middagpauze met je collega's over het pakketje dat je kan bezorgen.")
    type("2 collega's zijn super enthousiast.")
    type("Ze vinden het goed van je dat jij je steentje bijdraagt aan een duurzamere samenleving.")
    type("Een andere collega vindt het zeer nutteloos.")
    type("Je krijgt opmerkingen naar je hoofd zoals, daar heb je toch pakketbedrijven voor!")
    type("Je pauze is net voorbij en je krijgt de melding dat je binnen een uur moet beslissen of je het pakket gaat bezorgen. ")
    beloning_functie()


def beloning_2():
    type("Na je werk stap je in de auto en rij je langs de locatie waar je pakketje ophaalt. ")
    type("Deze locatie ligt op jou route naar huis. ")
    type("Vervolgens rij je een klein stukje om, om het pakketje langs te brengen. ")
    type("Je stapt uit, belt aan. En een hele aardige vrouw doet open. ")
    type("Ze is zo enthousiast dat je mee doet aan crowd logistics. Ze geeft je zelfs 5 euro fooi! ")
    type("Je rijdt naar huis en je krijgt het geld dezelfde avond nog bijgeschreven op je rekening. ")
    type("Twee dagen later krijg je opnieuw een melding van Crowd to Door of je een pakketje wil bezorgen.")
    type("Hiervoor moet je een kwartiertje omrijden op de fiets als je naar de voetbaltraining toegaat. ")
    type("Het is maar een klein pakketje. ")
    type("Je krijgt 5 euro beloning als je het pakketje aflevert, je moet 15 minuten omfietsen. ")


keuze2_einde = True


# Dit was het verhaal op basis van een beloning
# ________________________________________________________


# Dit is wanneer het verhaal eindigt als je het volledige verhaal doorloopt

def einde():
    type("Wat tof dat je wil blijven deelnemen aan crowd logistics! ")
    type("Ben je al geïnteresseerd om crowd logistics driver te worden? Neem dan eens een kijkje op dit platform.")
    type("Deze informatie wordt binnen een paar seconden voor je geopend!")
    type("Ondertussen sluit het programma vanzelf voor je af.")
    time.sleep(3)
    webbrowser.open('https://www.piggybee.com/nl/')
    quit()


# Dit is wanneer het verhaal eindigt als je NIET het volledige verhaal doorloopt
def einde_eerder():
    type("Wat tof dat je hebt deelgenomen aan crowd logistics, ontzettend bedankt!")
    type("We willen je heel graag nog wat meer informatie meegeven rondom crowd logistics.")
    type("Deze informatie wordt binnen een paar seconden voor je geopend!")
    type("Ondertussen sluit het programma vanzelf voor je af.")
    time.sleep(3)
    webbrowser.open('https://vil.be/en/project/crowd-logistics/')
    quit()


# Keuze beloning of intrinsieke motivatie
while keuze_intrinsiek_of_beloning:
    keuze_intrinsiek_of_beloning = input(
        "\nHeb jij een vorm van beloning nodig om deel te nemem aan dit soort duurzame alternatieven? (kies ja of nee) ").lower()
    if keuze_intrinsiek_of_beloning == 'ja':
        beloning()
        break
    elif keuze_intrinsiek_of_beloning == 'nee':
        intrinsiek()
        break
    else:
        type("dat is geen geldige keuze! je moet ja of nee kiezen")
        keuze_intrinsiek_of_beloning
        continue


# Keuze om het het laatste pakketje te bezorgen. (beide verhalen)
while keuze2_einde:
    keuze2_einde = input(
        "\nGa jij ook dit pakketje bezorgen? (kies ja of nee) ").lower()
    if keuze2_einde == "ja":
        einde()

    elif keuze2_einde == "nee":
        einde_eerder()

    else:
        type("dat is geen geldige keuze! je moet ja of nee kiezen")
        keuze2_einde
        continue
