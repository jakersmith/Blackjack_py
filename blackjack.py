import time
from src.deck import Deck
from src.card import Card


class Blackjack:
    def __init__(self):
        self.__hands = [[], []]
        self.__account = 100
        self.__bet = self.__account + 1
        self.__playerValue = 0
        self.__dealerValue = 0
        self.__deck = Deck()

    def playGame(self):
        user = "y"
        while self.__account > 0 and user == "y":
            # Resetting values and lists for each game
            self.__playerValue = 0
            self.__dealerValue = 0
            self.__bet = self.__account + 1
            self.__hands[0] = []
            self.__hands[1] = []

            self.__betting()
            self.__dealCards()
            self.__playerTurn()
            if self.__playerValue <= 21:
                self.__dealerTurn()
            if self.__playerValue <= 21 and self.__dealerValue <= 21:
                self.__determineWinner()
            if self.__account > 0:
                print("Your account balance is $", self.__account)
                user = str.lower(input("Would you like to play again? (Y or N) "))
                if user != "y":
                    break
        print("Thank you for playing!")
        print("Final balance = $", self.__account)


    def __betting(self):
        print("Your current balance is $", self.__account)
        if self.__account >= 5:
            while self.__bet > self.__account or self.__bet < 5:
                self.__bet = int(input("Your bet must be between $5 and your account balance.\nHow much would you like"
                                     " to bet? "))
        else:
            print("The your bet is ", self.__account)
            self.__bet = self.__account

    def __dealCards(self):
        self.__deck.shuffle()
        for i in range(2):
            self.__hands[0].append(self.__deck.draw())
            self.__hands[1].append(self.__deck.draw())
        print("The dealers second card is: ", self.__hands[1][1], '\n')

    def __playerTurn(self):
        print("Your Hand:", '\n', self.__hands[0][0], '\n', self.__hands[0][1],'\n')
        self.__getPlayerValue()
        hit = ""
        while hit == "":
            hit = str(input("Press ENTER to hit or type anything to stay" ))
            print('\n')
            if hit == "":
                self.__hands[0].append(self.__deck.draw())
                self.__playerValue += self.__hands[0][len(self.__hands[0]) - 1].getCardValue()
            if self.__playerValue <= 21:
                print("Your Hand:")
                for i in range(len(self.__hands[0])):
                    print(self.__hands[0][i])
                print('\n')
            else:
                print("You bust!", '\n')
                print("Your Hand:")
                for i in range(len(self.__hands[0])):
                    print(self.__hands[0][i])
                print('\n')
                self.__account -= self.__bet
                break

    def __dealerTurn(self):
        self.__dealerValue = 0
        print("Dealer's Hand:")
        print(self.__hands[1][0])
        print(self.__hands[1][1], '\n')
        self.__getDealerValue()
        while self.__dealerValue < 17:
            print("Dealer takes a card")
            time.sleep(1)
            self.__hands[1].append(self.__deck.draw())
            self.__dealerValue += self.__hands[1][len(self.__hands[1]) - 1].getCardValue()
        if self.__dealerValue <= 21:
            print("Dealer holds", '\n')
        else:
            print("Dealer busts", '\n')
            self.__account += self.__bet

    def __determineWinner(self):
        print("Dealer's Hand:")
        for i in range(len(self.__hands[1])):
            print(self.__hands[1][i])
        print('\n')
        if self.__playerValue > self.__dealerValue:
            print("You win!")
            print('\n')
            self.__account += self.__bet
        elif self.__playerValue == self.__dealerValue:
            print("It's a tie!")
            print('\n')
        elif self.__playerValue < self.__dealerValue:
            print("You lost!")
            print('\n')
            self.__account -= self.__bet

    def __playAgain(self):
        print("Your account balance is $", self.__account)
        if self.__account > 0:
            user = str.lower("Would you like to play again? (Y or N)")
            if user != "y":
                print("Thank you for playing!")
                print("Final balance = $", self.__account)

    def __getPlayerValue(self):
        for i in range(len(self.__hands[0])):
            self.__playerValue += self.__hands[0][i].getCardValue()
        return self.__playerValue

    def __getDealerValue(self):
        for i in range(len(self.__hands[1])):
            self.__dealerValue += self.__hands[1][i].getCardValue()
        return self.__dealerValue
