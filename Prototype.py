from itertools import chain
from time import sleep
import webbrowser

# typewriter effect
KPS = 20  # Aantal karakters per seconde


def type(text, delay=1/KPS):
    for line in text.splitlines():
        interval = len(line) + 1
        print('')
        for i in chain(range(interval)):
            print('\r' + line[:i], end="", flush=True)
            sleep(delay)


def opening():
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


keuze1 = -True
# Hier ga je verder als je een beloning nodig hebt


def beloning():
    type("Je scrolt over je Facebook tijdlijn en je ziet een advertentie voorbijkomen van Crowd to door.")
    type("Crowd to door is een online crowd logistics platform.")
    type("Je ziet dat je lekker kan bijverdienen door pakketjes af te leveren bij mensen als je toch al onderweg bent.")
    type("Dit is een leuke bijverdienste en je schrijft je dus in!")
    type("Binnen 2 dagen krijg je een oproep om een pakketje af te leveren als je uit je werk komt.")
    type("Hiervoor ben je 20 minuten langer onderweg en levert het je 10 euro op.")
    type("Je hebt in de middagpauze met je collega's over het pakketje dat je kan bezorgen.")
    type("2 collega's zijn super enthousiast, ze vinden het een leuk verdienconcept en je draagt je steentje bij aan een duurzamere samenleving.")
    type("Een andere collega vindt het zeer nutteloos, je krijgt opmerkingen naar je hoofd zoals, daar heb je toch pakketbedrijven voor!")
    type("Je pauze is net voorbij en je krijgt de melding dat je binnen een uur moet beslissen of je het pakket gaat bezorgen. ")


keuze2 = True


def beloning_2():
    type("Je pauze is net voorbij en je krijgt de melding dat je binnen een uur moet beslissen of je het pakket gaat bezorgen. ")


# Hier ga je verder als je het op basis van intrinsieke motivatie al zou doen!
def intrinsiek():
    type("In dit verhaal ga voor jou pakketje.")


def einde():
    type("Wat tof dat je hebt deelgenomen aan crowd logistics!")
    type("Ondanks dat je bent afgehaakt willen je toch nog wat informatie meegeven rondom crowd logistics.")
    print("\nDeze informatie wordt nu voor je geopend",
          webbrowser.open('https://vil.be/en/project/crowd-logistics/'))


# Keuze beloning of intrinsieke motivatie
while keuze1 == True:
    keuze1 = input(
        "\nNu zijn wij heel benieuwd! Heb jij een vorm van beloning nodig om deel te nemem aan dit soort duurzame alternatieven? ")
    if keuze1 == 'ja':
        beloning()
    elif keuze1 == 'nee':
        intrinsiek()
    else:
        type("dat is geen geldige keuze! je moet ja of nee kiezen")
        keuze1


while keuze2:
    keuze2 = input("Nu is de vraag, ga jij het pakketje bezorgen? ")
    if keuze2 == "ja":
        beloning_2()
    if keuze2 == "nee":
        einde()
    else:
        type("dat is geen geldige keuze! je moet ja of nee kiezen")
        keuze2
