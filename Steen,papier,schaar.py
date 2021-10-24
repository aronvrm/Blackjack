#
# wk1ex2a.py
#

import random
import time
# importeer de module met de naam random


def rps():

    print('\nWe gaan vandaag steen, papier,schaar spelen tegen de computer!')

    computer = random.choice(['steen', 'papier', 'schaar'])

    player = input("\nKies je wapen (steen, papier of schaar):")

    def opnieuw_spelen():

        while True:
            spelen = input(
                "wil je nog een keer spelen? (type ja als je nog een keer wil) ")
            spelen = spelen.lower()
            if spelen == ('ja'):
                rps()

            else:
                print('Bedankt voor het spelen, het spel sluit zich over 5 seconden af.')
                time.sleep(5)
                exit()

    while True:

        # steen
        if player == ('steen') and computer == ('papier'):
            print('Je verliest, de computer had papier.')
            opnieuw_spelen()

        elif player == ('steen') and computer == ('steen'):
            print('Het is een gelijkspel, de computer had ook steen!')
            opnieuw_spelen()

        elif player == ('steen') and computer == ('schaar'):
            print('Je wint! de computer had schaar.')
            opnieuw_spelen()

        # papier
        if player == ('papier') and computer == ('steen'):
            print('Je wint! de computer had steen.')
            opnieuw_spelen()

        elif player == ('papier') and computer == ('papier'):
            print('Het is een gelijkspel, de computer had ook papier!')
            opnieuw_spelen()

        elif player == ('papier') and computer == ('schaar'):
            print('Je verliest! de computer had schaar.')
            opnieuw_spelen()

        # schaar
        if player == ('schaar') and computer == ('steen'):
            print('Je verliest! de computer had steen.')
            opnieuw_spelen()

        elif player == ('schaar') and computer == ('schaar'):
            print('Het is een gelijkspel, de computer had ook schaar!')
            opnieuw_spelen()

        elif player == ('schaar') and computer == ('papier'):
            print('Je wint! de computer had papier.')
            opnieuw_spelen()

        else:
            print('Je keuze is niet correct, probeer het opnieuw')
            opnieuw_spelen()


rps()
