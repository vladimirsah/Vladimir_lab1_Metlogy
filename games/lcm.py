import math
import random

from game_engine import run_game


def game_logic():
    numbers = random.sample(range(1, 20), 3)
    question = " ".join(map(str, numbers))
    correct_answer = math.lcm(*numbers)
    return question, correct_answer


def play_lcm():
    description = "Find the smallest common multiple of given numbers."
    run_game(game_logic, description)
