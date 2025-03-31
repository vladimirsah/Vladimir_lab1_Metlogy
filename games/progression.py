import random

from game_engine import run_game


def generate_progression():
    start = random.randint(1, 10)
    ratio = random.randint(2, 5)
    length = random.randint(5, 10)
    progression = [start * (ratio**i) for i in range(length)]
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    return " ".join(map(str, progression)), correct_answer


def play_progression():
    description = "What number is missing in the progression?"
    run_game(generate_progression, description)
