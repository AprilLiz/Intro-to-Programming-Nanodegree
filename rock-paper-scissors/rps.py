#!/usr/bin/env python3
import random
"""This program plays a game of Rock, Paper, Scissors between two Players,
and reports both Player's scores each round."""


class Player:
    """The Player class is the parent class for all the Players
    in this game"""
    moves = ['rock', 'paper', 'scissors']

    def __init__(self):
        self.my_move = self.moves
        self.their_move = random.choice(self.moves)

    def move(self):
        """A computer player that always plays 'rock'"""
        return 'rock'

    def learn(self, my_move, their_move):
        """A remembering method used to tell each
        player what the other player's move was."""
        self.my_move = my_move
        self.their_move = their_move


class RandomPlayer(Player):
    """A computer player that chooses its moves randomly."""
    def move(self):
        return random.choice(self.moves)


class ReflectPlayer(Player):
    """A computer player that remembers and imitates what
    the human player did in the previous round."""
    def move(self):
        return self.their_move


class CyclePlayer(Player):
    """A computer player that cycles through the three moves"""
    def move(self):
        if self.my_move == self.moves[0]:
            return self.moves[1]
        elif self.my_move == self.moves[1]:
            return self.moves[2]
        else:
            return self.moves[0]


class HumanPlayer(Player):
    def move(self):
        while True:
            human_move = input("Rock, paper, scissors? > ")
            if human_move.lower() in self.moves:
                return human_move.lower()
            elif human_move.lower() == 'quit':
                print("Goodbye!")
                exit()


def beats(one, two):
    return ((one == 'rock' and two == 'scissors') or
            (one == 'scissors' and two == 'paper') or
            (one == 'paper' and two == 'rock'))


class Game:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.score1 = 0
        self.score2 = 0

    def rounds(self):
        """Takes user input as the number of rounds per game"""
        while True:
            self.how_many_rounds = input(
                "Please enter how many rounds you want to play: (use digits) ")
            if self.how_many_rounds.isdigit():
                return self.how_many_rounds
            elif self.how_many_rounds == 'quit':
                print("Goodbye!")
                exit()

    def play_round(self):
        move1 = self.p1.move()
        move2 = self.p2.move()
        print(f"You played {move1}.\nOpponent played {move2}.")
        if move1 == move2:
            print("***TIE***")
            self.score1 += 0
            self.score2 += 0
        elif beats(move1, move2):
            self.score1 += 1
            self.score2 += 0
            print("***PLAYER ONE WINS***")
        elif beats(move2, move1):
            self.score1 += 0
            self.score2 += 1
            print("***PLAYER TWO WINS***")
        print(f"Score: Player One {self.score1}, Player Two {self.score2}\n")
        self.p1.learn(move1, move2)
        self.p2.learn(move2, move1)

    def play_game(self):
        print("Rock Paper Scissors, Go!"
              "\nTo end the game enter 'quit' anytime.")
        self.rounds()
        for round in range(int(self.how_many_rounds)):
            print(f"Round {round + 1}:")
            self.play_round()
        if self.score1 == self.score2:
            print("***This game ended in a TIE!***")
        elif self.score1 > self.score2:
            print("$$$ The winner of this game is Player One! "
                  "Congratulations! $$$")
        elif self.score1 < self.score2:
            print("$$$ The winner of this game is Player Two! "
                  "Congratulations! $$$")
        print(f"Final scores: Player One [{self.score1}]"
              f" Player Two [{self.score2}]"
              "\n>>>GAME OVER<<<")


if __name__ == '__main__':
    game = Game(HumanPlayer(), random.choice(
           [RandomPlayer(), ReflectPlayer(), CyclePlayer(), Player()]))
    game.play_game()
