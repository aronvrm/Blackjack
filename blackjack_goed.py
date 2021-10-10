def blackjack():

    import random

    suits = ('Harten', 'Ruiten', 'Klaver', 'Schoppen')
    ranks = ('Twee', 'Drie', 'Vier', 'Vijf', 'Zes', 'Zeven',
             'Acht', 'Negen', 'Tien', 'Boer', 'Vrouw', 'Koning', 'Aas')
    values = {'Twee': 2, 'Drie': 3, 'Vier': 4, 'Vijf': 5, 'Zes': 6, 'Zeven': 7, 'Acht': 8,
              'Negen': 9, 'Tien': 10, 'Boer': 10, 'Vrouw': 10, 'Koning': 10, 'Aas': 11}

    playing = True

    class Card:

        def __init__(self, suit, rank):
            self.suit = suit
            self.rank = rank

        def __str__(self):
            return self.rank + ' van ' + self.suit

    class Deck:

        def __init__(self):
            self.deck = []  # start with an empty list
            for suit in suits:
                for rank in ranks:
                    # build Card objects and add them to the list
                    self.deck.append(Card(suit, rank))

        def __str__(self):
            deck_comp = ''  # start with an empty string
            for card in self.deck:
                deck_comp += '\n '+card.__str__()  # add each Card object's print string
            return 'Het dek heeft:' + deck_comp

        def shuffle(self):
            random.shuffle(self.deck)

        def deal(self):
            single_card = self.deck.pop()
            return single_card

    class Hand:

        def __init__(self):
            self.cards = []  # start with an empty list as we did in the Deck class
            self.value = 0   # start with zero value
            self.aces = 0    # add an attribute to keep track of aces

        def add_card(self, card):
            self.cards.append(card)
            self.value += values[card.rank]
            if card.rank == 'Aas':
                self.aces += 1  # add to self.aces

        def adjust_for_ace(self):
            while self.value > 21 and self.aces:
                self.value -= 10
                self.aces -= 1

    class Chips:

        def __init__(self):
            self.total = 100  # This can be set to a default value or supplied by a user input
            self.bet = 0

        def win_bet(self):
            self.total += self.bet

        def lose_bet(self):
            self.total -= self.bet

    def take_bet(chips):

        while True:
            try:
                chips.bet = int(
                    input("Hoeveel chips wil je inzetten? "))
            except ValueError:
                print("Je moet wel een heel getal invoeren. ")
            else:
                if chips.bet > chips.total:
                    print(
                        "Sorry, je hebt niet genoeg geld om in te zetten! Je hebt: ", chips.total)
                else:
                    break

    def hit(deck, hand):
        hand.add_card(deck.deal())
        hand.adjust_for_ace()

    def hit_or_stand(deck, hand):
        global playing  # to control an upcoming while loop

        while True:
            x = input(
                "Doorgaan of stoppen? Klik op h om door te gaan of s om te stoppen  ")

            if x[0].lower() == 'h':
                hit(deck, hand)  # hit() function defined above

            elif x[0].lower() == 's':
                print("De speler stopt, het is de nu de dealers beurt.")
                playing = False

            else:
                print("Sorry, je hebt geen correcte optie gekozen, probeer het opnieuw.")
                continue
            break

    def show_some(player, dealer):
        print("\nDealer's hand:")
        print("(Verborgen kaart)")
        print('', dealer.cards[1])
        print("\nSpelers hand::", *player.cards, sep='\n ')

    def show_all(player, dealer):
        print("\nDealer's hand:", *dealer.cards, sep='\n ')
        print("Dealer's hand =", dealer.value)
        print("\nSpelers hand:", *player.cards, sep='\n ')
        print("Spelers hand =", player.value)

    def player_busts(player, dealer, chips):
        print("Je bent gebust!")
        chips.lose_bet()

    def player_wins(player, dealer, chips):
        print("Je wint!")
        chips.win_bet()

    def dealer_busts(player, dealer, chips):
        print("De dealer bust, jij wint!")
        chips.win_bet()

    def dealer_wins(player, dealer, chips):
        print("De dealer wint!")
        chips.lose_bet()

    def push(player, dealer):
        print("Dealer en speler hebben een push! Je krijgt je inzet terug!.")

    player_chips = Chips()  # remember the default value is 100

    while True:
        # Print an opening statement
        print('\nWelkom bij Blackjack! Kom zo dicht mogelijk bij de 21 zonder eroverheen te gaan!\nDe dealer gaat door tot ze 17 bereikt. Azen tellen als 1 of 11.')
        print("\nJe chip totaal is: ", player_chips.total)

        # Create & shuffle the deck, deal two cards to each player
        deck = Deck()
        deck.shuffle()

        player_hand = Hand()
        player_hand.add_card(deck.deal())
        player_hand.add_card(deck.deal())

        dealer_hand = Hand()
        dealer_hand.add_card(deck.deal())
        dealer_hand.add_card(deck.deal())

        # Prompt the Player for their bet
        take_bet(player_chips)

        # Show cards (but keep one dealer card hidden)
        show_some(player_hand, dealer_hand)

        while playing:  # recall this variable from our hit_or_stand function

            # Prompt for Player to Hit or Stand
            hit_or_stand(deck, player_hand)

            # Show cards (but keep one dealer card hidden)
            show_some(player_hand, dealer_hand)

            # If player's hand exceeds 21, run player_busts() and break out of loop
            if player_hand.value < 21:
                hit_or_stand(deck, player_hand)

            elif player_hand.value < 21:
                hit_or_stand(deck, player_hand)

            elif player_hand.value < 21:
                hit_or_stand(deck, player_hand)

            elif player_hand.value < 21:
                hit_or_stand(deck, player_hand)

            elif player_hand.value < 21:
                hit_or_stand(deck, player_hand)

            elif player_hand.value > 21:
                player_busts(player_hand, dealer_hand, player_chips)
                break

        # If Player hasn't busted, play Dealer's hand until Dealer reaches 17

            if player_hand.value <= 21:

                while dealer_hand.value < 17:
                    hit(deck, dealer_hand)

                # Show all cards
                show_all(player_hand, dealer_hand)

                # Run different winning scenarios
                if dealer_hand.value > 21:
                    dealer_busts(player_hand, dealer_hand, player_chips)

                elif dealer_hand.value > player_hand.value:
                    dealer_wins(player_hand, dealer_hand, player_chips)

                elif dealer_hand.value < player_hand.value:
                    player_wins(player_hand, dealer_hand, player_chips)

                else:
                    push(player_hand, dealer_hand)

            # Inform Player of their chips total
            print("\nJe chip totaal is: ", player_chips.total)

            # Ask to play again
            new_game = input(
                "Klaar voor een nieuwe ronde? ")

            if new_game[0].lower() == '':
                playing = True
                continue
            else:
                print("Bedankt voor het spelen!")
                break


blackjack()
