def run_game(game_logic, description):
    """Движок."""
    print("Welcome!")
    name = input("Say your name? ")
    print(f"Hello, {name}!")
    print(description)

    for _ in range(3):
        question, correct_answer = game_logic()
        print(f"Question: {question}")

        user_answer = input("Your answer: ")
        if user_answer.isdigit() and int(user_answer) == correct_answer:
            print("Correct!")
        else:
            print(
                f"'{user_answer}' is wrong ;(. "
                f"Correct '{correct_answer}'."
            )
            print(f"Let's try again, {name}!")
            return

    print(f"Super, {name}!")