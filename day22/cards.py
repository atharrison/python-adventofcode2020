class PlayerDeck:
    def __init__(self, player_num, start_deck):
        self.player_num = player_num
        self.deck = start_deck

    def add_to_bottom(self, card):
        # print(f"Adding {card} to Player {self.player_num}")
        self.deck.append(card)

    def has_lost(self):
        return len(self.deck) == 0

    def can_recurse(self, depth):
        return len(self.deck) >= depth

    def get_recursive_deck(self, depth):
        return self.deck[0:depth].copy()

    def play_next_card(self):
        card = self.deck[0]
        self.deck = self.deck[1:]
        return card

    def score(self):
        size = len(self.deck)
        multiplier = size
        total = 0
        while multiplier > 0:
            total += multiplier * self.deck[size - multiplier]
            multiplier -= 1

        return total

    def __str__(self):
        return f"Player {self.player_num}'s deck: {self.deck}"

    def __repr__(self):
        return self.__str__()
