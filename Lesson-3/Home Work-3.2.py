lists_to_test = [
    [12, 3, 4, 10],
    [1],
    [],
    [12, 3, 4, 10, 8]
]


def move_last_to_front(lst):
    if len(lst) <= 1:
        return lst
    return [lst[-1]] + lst[:-1]


for test_list in lists_to_test:
    result = move_last_to_front(test_list)
    print("Було:", test_list, "=> Стало:", result)