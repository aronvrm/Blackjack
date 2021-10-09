
def blackjack():

    import random
    from random import shuffle

    kleuren = ('Harten', 'Ruiten', 'Klaver', 'Schoppen')

    getal = ('Twee', 'Drie', 'Vier', 'Vijf', 'Zes', 'Zeven',
             'Acht', 'Negen', 'Tien', 'Boer', 'Vrouw', 'Koning', 'Aas')

    waarden = {'Twee': 2, 'Drie': 3, 'Vier': 4, 'Vijf': 5, 'Zes': 6, 'Zeven': 7, 'Acht': 8,
               'Negen': 9, 'Tien': 10, 'Boer': 10, 'Vrouw': 10, 'Koning': 10, 'Aas': 11}

    playing = True

    class Kaart:

        def __init__(self, kleur, getallen):
            self.kleur = kleur
            self.getallen = getallen

        def __str__(self):
            return self.getallen + " van " + self.kleur

    # dek kaarten

    class Deck:

        def __init__(self):
            self.deck = []  # empty list
            for kleur in kleuren:
                for getallen in getal:

                    self.deck.append(Kaart(kleur, getallen))

        def __str__(self):
            deck_sam = ''
            for kaart in self.deck:
                deck_sam += '\n' + kaart.__str__()
            return "Het dek heeft:" + deck_sam

            # shuffle de kaarten

        def shuffle(self):
            random.shuffle(self.deck)

        def delen(self):
            enkele_kaart = self.deck.pop()
            return enkele_kaart

    # hand
    class Hand:
        def __init__(self):
            self.kaarten = []
            self.waarde = 0
            self.aas = 0

        def voeg_kaart_toe(self, kaart):
            self.kaarten.append(kaart)
            self.waarde += waarden[kaart.getallen]
            if kaart.getallen == 'Aas':
                self.aas += 1

        def aanpassing_voor_aas(self):

            # als de waarde >21 is verander naar een 1
            while self.waarde > 21 and self.aas:
                self.waarde -= 10
                self.aas -= 1

    # chips

    class Chips:

        def __init__(self):
            self.totaal = 100
            self.wedden = 0

        def win_weddenschap(self):
            self.totaal += self.wedden

        def verlies_weddenschap(self):
            self.totaal -= self.wedden

    def neem_weddenschap(chips):

        while True:

            try:
                chips.weddenschap = int(
                    input("Hoeveel chips wil je inzetten? (je start met 100)  "))
            except ValueError:
                print("Je moet wel een heel getal invoeren.")
            else:
                if chips.weddenschap > chips.totaal:
                    print('Sorry, je hebt niet genoeg geld om in te zetten! Je hebt: {}'.format(
                        chips.totaal))
                else:
                    break

    # hit
    def hit(deck, hand):

        hand.voeg_kaart_toe(deck.delen())
        hand.aanpassing_voor_aas()

    def hit_of_stoppen(deck, hand):
        global playing

        while True:
            x = input(
                'Doorgaan of stoppen? Klik op "h" om door te gaan of "s" om te stoppen  ')

            if x[0].lower() == 'h':
                hit(deck, hand)

            elif x[0].lower() == 's':
                print('De speler stopt, het is de nu de dealers beurt.')
                playing = False

            else:
                print('Sorry, je hebt geen correcte optie gekozen, probeer het opnieuw.')
                continue
            break

    # Functie om kaarten te tonen

    def laat_sommige_zien(dealer, speler):

        print("\nDealers hand:")
        print("Eerste kaart is verborgen")
        print(dealer.kaarten[1])

        # alle kaarten
        print("\nSpelers hand:")
        for kaart in speler.kaarten:
            print(kaart)

    def laat_alles_zien(dealer, speler):

        print("\n Dealers hand:")
        for kaart in speler.kaarten:
            print(kaart)
        print('Dealers hand: {dealer.waarde}')

        print("\n Spelers hand:")
        for kaart in speler.kaarten:
            print(kaart)
        print('Spelers hand: {speler.waarde}')

    # game scenarios

    def speler_bust(speler, dealer, chips):
        print('Speler bust')
        chips.verlies_weddenschap()

    def speler_wint(speler, dealer, chips):
        print('Jij wint!')
        chips.win_weddenschap()

    def dealer_bust(speler, dealer, chips):
        print('Jij wint, de dealer busted!')
        chips.win_weddenschap()

    def dealer_wint(speler, dealer, chips):
        print('Dealer wint')
        chips.verlies_weddenschap()

    def push(speler, dealer):
        print('Het is een gelijkspel, dus een Push. Je krijgt je inzet terug.')

    while True:
        print('Welkom bij Blackjack! Kom zo dicht mogelijk bij de 21 zonder eroverheen te gaan!\n\
    Dealer gaat door tot ze 17 bereikt. Azen tellen als 1 of 11.')

        # hand
        deck = Deck()
        deck.shuffle()

        speler_hand = Hand()
        speler_hand.voeg_kaart_toe(deck.delen())
        speler_hand.voeg_kaart_toe(deck.delen())

        dealer_hand = Hand()
        dealer_hand.voeg_kaart_toe(deck.delen())
        dealer_hand.voeg_kaart_toe(deck.delen())

        # chips
        spelers_chips = Chips()

        # weddenschap
        neem_weddenschap(spelers_chips)

        # kaarten zien
        laat_sommige_zien(speler_hand, dealer_hand)

        while playing:

            hit_of_stoppen(deck, speler_hand)

            # show cards
            laat_sommige_zien(speler_hand, dealer_hand)

            # bust speler
            if speler_hand.waarde > 21:
                speler_bust(speler_hand, dealer_hand, spelers_chips)
                break

        # speler bust niet, dealer speelt

        if speler_hand.waarde <= 21:
            while dealer_hand.waarde < 17:
                hit(deck, dealer_hand)

            # show alle kaarten dealer
            laat_alles_zien(speler_hand, dealer_hand)

            # verschillende winnen scenarios
            if dealer_hand.waarde > 21:
                dealer_bust(speler_hand, dealer_hand, spelers_chips)
            elif dealer_hand.waarde > speler_hand.waarde:
                dealer_wint(speler_hand, dealer_hand, spelers_chips)
            elif dealer_hand.waarde < speler_hand.waarde:
                speler_wint(speler_hand, dealer_hand, spelers_chips)
            else:
                push(speler_hand, dealer_hand)

                # informeren nieuwe chips

        print('\nJe chipaantal is: {}'.format(spelers_chips.totaal))

        nieuw_spel = input(
            'Wil je nog een keer spelen? (y om nog een keer te spelen')

        if nieuw_spel[0].lower() == 'y':
            playing = True
            continue
        else:
            ("Bedankt voor het spelen!")
            break


blackjack()
