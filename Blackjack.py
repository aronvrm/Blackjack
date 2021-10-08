
def blackjack():

    import random
    from random import shuffle

    class kaart():

        def __init__(self, kleur, getallen):
            self.kleur = kleur
            self.getallen = getallen

        def __str__(self):
            return self.getallen + " van " + self.kleur

    # dek kaarten

    kleuren = ('Harten', 'Ruiten', 'Klaver', 'Schoppen')

    getal = ('Twee', 'Drie', 'Vier', 'Vijf', 'Zes', 'Zeven',
             'Acht', 'Negen', 'Tien', 'Boer', 'Vrouw', 'Koning', 'Aas')

    waarden = {'Twee': 2, 'Drie': 3, 'Vier': 4, 'Vijf': 5, 'Zes': 6, 'Zeven': 7, 'Acht': 8,
               'Negen': 9, 'Tien': 10, 'Boer': 10, 'Vrouw': 10, 'Koning': 10, 'Aas': 11}

    playing = True

    class Deck:

        def __init__(self):

            self.alle_kaarten = []  # empty list

            for kleur in kleuren:
                for getallen in getal:

                    # kaart genereren
                    self.alle_kaarten.append(kaart(kleur, getallen))

        def __str__(self):
            deck_sam = ''
            for kaart in self.deck:
                deck_sam += '\n' + kaart.__str__()
            return "Het dek heeft:" + deck_sam

            # shuffle de kaarten

        def schudden(self):
            random.shuffle(self.alle_kaarten)

        def delen(self):
            enkele_kaart = self.Deck.pop()
            return enkele_kaart

    # hand
    class Hand:
        def __init__(self):
            self.kaart = []
            self.waarde = 0
            self.aas = 0

        def voeg_kaart_toe(self, kaart):
            self.kaart.append(kaart)
            self.waarde += waarden[kaart.waarde]

            # track ace
            if kaart.waarden == 'Aas':
                self.aas += 1

        def aanpassing_voor_aas(self):

            # als de waarde >21 is verander naar een 1
            while self.waarde > 21 and self.aas:
                self.waarde -= 10
                self.aas -= 1

    test_deck = Deck()
    test_deck.schudden()

    test_player = Hand()
    pulled_card = test_deck.delen()
    print(pulled_card)
    test_player.voeg_kaart_toe(pulled_card)
    print(test_player.waarde)

    test_player.voeg_kaart_toe(test_deck.delen)

    # chips

    class Chips:

        def __init__(self, totaal=100):
            self.totaal = totaal
            self.wedden = 0

        def win_weddenschap(self):
            self.totaal += self.wedden

        def verlies_weddenschap(self):
            self.totaal -= self.wedden

    # dealen van de startkaarten

    # Verbergen van de gesloten kaart dealer

    # tonen beide kaarten speler

    # stoppen of doorgaan

    # als de speler niet doodgaat vragen om nog een kaart

    # als een speler stopt, moet de dealer doorgaan tot minimaal 17
    # winnaar bepalen en chips duidelijk verdelen
    # vragen of je nog een keer wil


blackjack()
