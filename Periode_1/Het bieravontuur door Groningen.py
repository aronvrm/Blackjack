"""
Titel voor je avontuur: De queeste naar taart.

Opmerkingen over hoe je het avontuuur kan "winnen" of "verliezen":
* kies de tafel om te winnen
* kies de deur om te verliezen
"""

import time


def adventure():
    """Runs one session of interactive fiction

    Well, it's "fiction," depending on the pill color chosen...

    arguments: no arguments (prompted text doesn't count as an argument)
    results: no results     (printing doesn't count as a result)
    """
    # zet deze waarde op 0.0 om te testen of snel te spelen,
    # ..of hoger voor meer dramatisch effect!
    delay = 0.0

    username = input("Hey avonturier, wat is je naam?? ")

    # intro
    print()
    print("Welkom,", username, "in het mooie Groningen, een labyrint")
    print("van gewichtige wonderen en grote hoeveelheden ... bier!")
    print()
    print("Uw queeste is: om een biertje te vinden, en te drinken!")
    print()

    # Smaak bier (if,elif,else)
    flavor = input("Welke biertje zoekt u? ")
    if flavor == "hertog jan":
        print("Uw wijsheid in bier is overweldigend!")
    elif flavor == "heineken":
        print("dat kan er nog net mee door")
    else:
        print("ieder zijn smaak...")

    print()
    print("Voorwaarts naar de queeste!\n\n")

    # Hoeveel (if en else)
    Bierkes = input("Maar hoeveel biertjes zoekt u hiervan? ")
    if Bierkes == ("1" or "2"):
        print("Dat is weinig maar oke ")
    else:
        print("Kijk gei zeit een bierpersoon!")

    print("Een gang strekt zich voor u uit; in het gedimde licht ziet u")
    print("een biertje zonder merk")
    print("En aan de andere kant ziet u")
    print("Zonder merk")

    # Keuze (if en elif)
    Keuze = input("Welke van de twee biertjes heeft u keuze, links of rechts?")
    if Keuze == "links":
        print("Dat is jouw lekker gekozen biertje!")
    elif Keuze == "rechts":
        print("Helaas, nu krijgt gij pittbier")

    # if elif (3) & else

    Bierkeuze = input("Zeit gij tevreden met u bier?")

    if Bierkeuze == "ja":
        print("Dat is fijn, mogen wij u dan nog een een vraag stellen over dit spel?")

    elif Bierkeuze == 'nee':
        print("Dan wensen wij u een fijne dag verder!")

    elif Bierkeuze == 'misschien':
        print('Dan vragen we je het de volgende keer hoe je biertje was! Geniet van je biertje.')

    else:
        print("Dat was het voor vandaag! Geniet van uw biertje!")


adventure()
