from .cards import PlayerDeck


class Day22:
    # Solved the next afternoon, with the kids
    def __init__(self, data):
        self.raw_data = data

    def solve_part1(self):
        self.decks = {}
        self.load_decks()
        print(f"Deck keys: {self.decks.keys()}")
        print(self.decks)
        winner = self.play_game(self.decks[1], self.decks[2])
        self.print_score(winner)

    def solve_part2(self):
        self.decks = {}
        self.load_decks()
        print(self.decks)
        winner, game = self.play_game_recursive(self.decks[1], self.decks[2], 1)
        self.print_score(winner)

    def print_score(self, deck):
        print("== Post-game results ==")
        print(f"Winner: {deck.player_num} Score: {deck.score()}")

    def load_decks(self):
        deck = None
        for line in self.raw_data:
            if line.startswith("Player"):
                player_num = line.split(" ", 2)[1][0]
                print(f"Player: {player_num}")
                deck = PlayerDeck(player_num, [])
                self.decks[int(player_num)] = deck
            elif line == "":
                pass
            else:
                print(f"Print added {line} to Player {player_num}")
                deck.add_to_bottom(int(line))

    def play_game(self, p1, p2):
        round = 1
        game = 1
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

        if p1.has_lost():
            print(f"The winner of game {game} is player 2!")
            return p2
        print(f"The winner of game {game} is player 1!")
        return p1

    def game_state(self, p1, p2):
        return ":".join(str(i) for i in [*p1.deck, -1, *p2.deck])

    def play_game_recursive(self, p1, p2, game):
        game_states = set()
        round = 0
        next_game = game + 1
        print(f"=== Game {game} ===\n")
        while not p1.has_lost() and not p2.has_lost():
            round += 1
            print(f"-- Round {round} (Game {game}) --")
            print(p1)
            print(p2)
            new_state = self.game_state(p1, p2)
            if new_state in game_states:
                return p1, game
            else:
                game_states.add(self.game_state(p1, p2))

            card1 = p1.play_next_card()
            print(f"Player 1 plays: {card1}")
            card2 = p2.play_next_card()
            print(f"Player 2 plays: {card2}")

            if p1.can_recurse(card1) and p2.can_recurse(card2):
                game_states.add(new_state)
                newP1 = PlayerDeck(1, p1.get_recursive_deck(card1))
                newP2 = PlayerDeck(2, p2.get_recursive_deck(card2))

                print("Playing sub-game to determine the winner...\n")

                winner, next_game = self.play_game_recursive(newP1, newP2, next_game)
                next_game += 1
                print(f"... anyway, back to game {game}.")
                if winner.player_num == 1:
                    print(f"Player 1 wins round {round} of game {game}!\n")
                    p1.add_to_bottom(card1)
                    p1.add_to_bottom(card2)
                else:
                    print(f"Player 2 wins round {round} of game {game}!\n")
                    p2.add_to_bottom(card2)
                    p2.add_to_bottom(card1)

            else:
                if card1 > card2:
                    print(f"Player 1 wins round {round} of game {game}!\n")
                    p1.add_to_bottom(card1)
                    p1.add_to_bottom(card2)
                else:
                    print(f"Player 2 wins round {round} of game {game}!\n")
                    p2.add_to_bottom(card2)
                    p2.add_to_bottom(card1)

        if p1.has_lost():
            print(f"The winner of game {game} is player 2!")
            return p2, game
        print(f"The winner of game {game} is player 1!")
        return p1, game
