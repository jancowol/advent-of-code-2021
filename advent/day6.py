input = [1, 1, 3, 5, 1, 3, 2, 1, 5, 3, 1, 4, 4, 4, 1, 1, 1, 3, 1, 4, 3, 1, 2, 2, 2, 4, 1, 1, 5, 5, 4, 3, 1, 1, 1, 1, 1, 1, 3, 4, 1, 2, 2, 5, 1, 3, 5, 1, 3, 2, 5, 2, 2, 4, 1, 1, 1, 4, 3, 3, 3, 1, 1, 1, 1, 3, 1, 3, 3, 4, 4, 1, 1, 5, 4, 2, 2, 5, 4, 5, 2, 5, 1, 4, 2, 1, 5, 5, 5, 4, 3, 1, 1, 4, 1, 1, 3, 1, 3, 4, 1, 1, 2, 4, 2, 1, 1, 2, 3, 1, 1, 1, 4, 1, 3, 5, 5, 5, 5, 1, 2, 2, 1, 3, 1, 2, 5, 1, 4, 4, 5, 5, 4, 1, 1, 3, 3, 1, 5, 1, 1, 4, 1, 3, 3, 2, 4, 2, 4,
         1, 5, 5, 1, 2, 5, 1, 5, 4, 3, 1, 1, 1, 5, 4, 1, 1, 4, 1, 2, 3, 1, 3, 5, 1, 1, 1, 2, 4, 5, 5, 5, 4, 1, 4, 1, 4, 1, 1, 1, 1, 1, 5, 2, 1, 1, 1, 1, 2, 3, 1, 4, 5, 5, 2, 4, 1, 5, 1, 3, 1, 4, 1, 1, 1, 4, 2, 3, 2, 3, 1, 5, 2, 1, 1, 4, 2, 1, 1, 5, 1, 4, 1, 1, 5, 5, 4, 3, 5, 1, 4, 3, 4, 4, 5, 1, 1, 1, 2, 1, 1, 2, 1, 1, 3, 2, 4, 5, 3, 5, 1, 2, 2, 2, 5, 1, 2, 5, 3, 5, 1, 1, 4, 5, 2, 1, 4, 1, 5, 2, 1, 1, 2, 5, 4, 1, 3, 5, 3, 1, 1, 3, 1, 4, 4, 2, 2, 4, 3, 1, 1]


def count_many_generations(input, days):
    dict = {}
    for clock in input:
        fish_count_for_clock = dict.get(clock, 0)
        dict.update({clock: fish_count_for_clock + 1})

    dict2 = dict
    for i in range(days):
        dict2[-1] = dict2.get(0, 0)
        dict2[0] = dict2.get(1, 0)
        dict2[1] = dict2.get(2, 0)
        dict2[2] = dict2.get(3, 0)
        dict2[3] = dict2.get(4, 0)
        dict2[4] = dict2.get(5, 0)
        dict2[5] = dict2.get(6, 0)
        dict2[6] = dict2.get(7, 0)
        dict2[7] = dict2.get(8, 0)
        dict2[8] = dict2[-1]
        dict2[6] = dict2[6] + dict2[-1]
    result = sum(dict2.values()) - dict2[-1]
    return result


def calc(input, days):
    print(f'Count after {days} days: {count_many_generations(input, days)}')

calc(input, 80)
calc(input, 256)
