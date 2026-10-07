import random


class Player:
    def __init__(self, name):
        self.name = name
        self.cash = 100
        self.cards = []

    def buy(self, card, price):
        if self.cash >= price:
            self.cash -= price
            self.cards.append(card)
            return True
        return False

    def sell(self, card, price):
        if card in self.cards:
            self.cards.remove(card)
            self.cash += price
            return True
        return False


def deal(players, cards_per_player=5):
    """Shuffle the deck and deal cards to each player."""
    deck = ["A", "B", "C", "D"] * 10
    random.shuffle(deck)

    for player in players:
        player.cards = []
        for _ in range(cards_per_player):
            player.cards.append(deck.pop())


def show_positions(players):
    for player in players:
        print(player.name, "- cash:", player.cash, "- cards:", player.cards)


players = [Player("Alice"), Player("Bob")]
deal(players)

print("Starting positions")
show_positions(players)

# Example trade: Alice buys one of Bob's cards.
if players[1].cards:
    card = players[1].cards[0]
    price = 5

    if players[0].buy(card, price):
        players[1].sell(card, price)
        print("\nTrade:", players[0].name, "buys", card,
              "from", players[1].name, "for", price)

print("\nFinal positions")
show_positions(players)
