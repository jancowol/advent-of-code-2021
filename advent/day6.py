def count_many_generations(input, days):
    dict = {}
    for clock in input:
        fish_count_for_clock = dict.get(clock, 0)
        dict.update({clock: fish_count_for_clock + 1})

    print('********************')
    dict2 = dict
    print(dict2)
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
        print(dict2)
    result = sum(dict2.values()) - dict2[-1]
    return result
