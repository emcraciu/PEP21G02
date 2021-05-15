# form the pinball game results below we want to check which of the the hole numbers are missing considering number of
# holes in the table are

test_data = [[1, 2, 3], [3, 3, 5], [8, 9, 4], [2, 8, 4]]


def pinball_game(games_data: list, nr_holes: int = 10):  # we can provide both type hint and default value
    result = set()
    for game_result in games_data:
        result = result.union(set(game_result))
    holes_set = set(range(1, nr_holes + 1))
    return holes_set.difference(result)


print('The following holes are missing: ', pinball_game(test_data))
