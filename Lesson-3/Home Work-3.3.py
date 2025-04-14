def split_list(lst):

    if not lst:
        return [[], []]


    split_index = (len(lst) + 1) // 2
    return [lst[:split_index], lst[split_index:]]
test_lists = [
    [1, 2, 3, 4, 5, 6],
    [1, 2, 3],
    [1, 2, 3, 4, 5],
    [1],
    []
]

for test in test_lists:
    result = split_list(test)
    print("Було:", test, "=> Стало:", result)
