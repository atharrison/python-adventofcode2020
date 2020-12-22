from .cards import PlayerDeck


class Day22:
    # Solved the next afternoon, with the kids
    def __init__(self, data):
        self.raw_data = data
        self.decks = {}
        self.load_decks()

    def solve_part1(self):
        print(f"Deck keys: {self.decks.keys()}")
        print(self.decks)
        self.play_game()

    def solve_part2(self):
        pass

    def load_decks(self):
        deck = None
        for line in self.raw_data:
            if line.startswith("Player"):
                player_num = line.split(" ", 2)[1][0]
                print(f"Player: {player_num}")
                deck = PlayerDeck(player_num)
                self.decks[int(player_num)] = deck
            elif line == "":
                pass
            else:
                deck.add_to_bottom(int(line))

    def play_game(self):
        round = 1
        p1 = self.decks[1]
        p2 = self.decks[2]
        while not p1.has_lost() and not p2.has_lost():
            print(f"-- Round {round} --")
            print(p1)
            print(p2)
            round += 1
            card1 = p1.play_next_card()
            print(f"Player 1 plays: {card1}")
            card2 = p2.play_next_card()
            print(f"Player 2 plays: {card2}")

            if card1 > card2:
                print("Player 1 wins the round!\n")
                p1.add_to_bottom(card1)
                p1.add_to_bottom(card2)
            else:
                print("Player 2 wins the round!\n")
                p2.add_to_bottom(card2)
                p2.add_to_bottom(card1)

        print("== Post-game results ==")
        print(p1)
        print(p2)
        if p1.has_lost():
            print(f"P2 Score: {p2.score()}")
        else:
            print(f"P1 Score: {p1.score()}")
