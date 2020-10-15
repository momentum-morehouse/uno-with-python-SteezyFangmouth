from random
NUMBERS = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
COLORS = ["🔴","🟢","🟡","🔵"]
PLAYER_REF = {}
class Card:
    def __init__(self, number, color):
        self.number = number
        self.color = color
    def ___str___(self):
        return f"{self.color} {self.number}"   
class Player:
    def __init__(self, name, hand = []):
        self.name = name
        self.hand = hand
class Deck:
    def __init__(self, numbers, colors):
        self.cards = []
        for number in numbers:
            for color in colors:
                card = Card(number, color)
                self.cards.append(card)
                
class Game:
    #Shuffled Deck
    def __init__(self):
        self.deck = Deck(NUMBERS, COLORS)
        self.shuffled_deck = self.deck.shuffle()
        
    #Takes Card Off Top
    def getCard(self,deck):
        topCard = deck[0]
        deck.remove(deck[0])
        return topCard

    def deal_start_hand(self, number_of_players,deck):
        players = list(PLAYER_REF.values())
        for i in range(7):
            for current_player in players:
                print(len(current_player.hand))
                print("current_player")
                card = deck.pop()
                print(len(deck))

        return deck

def startGame():
@@ -102,15 +96,12 @@ def startGame():
            enough_players = True
    #Gives Starting Hand To All Players

    for key,value in PLAYER_REF.items():
        print(f"{key}'s hand = {value.hand}")

startGame