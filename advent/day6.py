
class Fish():
    def __init__(self, clock):
        self.clock = clock

    def day_tick(self):
        self.clock -= 1
        if(self.clock == -1):
            self.clock = 6
            return 8
        # if(self.clock )
        # return 8


def model_school_from_clocks(fish_clocks, days):
    school = [Fish(clock) for clock in fish_clocks]
    return model_school_spawn(school, days)


def count_many_generations(input):
    dict = {}
    for clock in input:
        fish_count_for_clock = dict.get(clock, 0)
        dict.update({clock: fish_count_for_clock + 1})

    print('********************')
    dict2 = dict
    print(dict2)
    for i in range(256):
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


def model_school_spawn(initial_school, simulation_days):
    school = initial_school
    for i in range(simulation_days):
        new_fish = [Fish(new_fish_age) for new_fish_age in (
            foo.day_tick() for foo in school) if new_fish_age != None]
        school += new_fish
    return school
