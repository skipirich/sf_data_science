"""Game - Predict the number
The program proposals a number and then predict it
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Random number to guesses

    Args:
        number (int, optional): Hidden number. Defaults to 1.

    Returns:
        int: Count of attempts
    """
    count = 0
    start = 1
    finish = 101
    while start != finish:
        count += 1
        predict_number = np.random.randint(start, finish)
        if number == predict_number:
            break
        elif number > predict_number:
            start = predict_number
        else:
            finish = predict_number
    return count


def score_game(random_predict) -> int:
    """How many average attempts required to predict the number

    Args:
        random_predict ([type]): the predict's function

    Returns:
        int: average count of attempts
    """
    count_ls = []
    random_array = np.random.randint(1, 101, size=(100)) 

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Your algorithm predicts the number in average for: {score} attempts")
    return score


if __name__ == "__main__":
    score_game(random_predict)
