def test_can_read_file():
    data = read_file('input')
    assert len(data) == 2000


def test_can_count_increases():
    data = get_readings()
    count = count_increases(data)
    assert count == 1374


def test_can_generate_windows():
    input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    window_groups = windows(input, 3)
    assert list(window_groups) == [
        [199, 200, 208],
        [200, 208, 210],
        [208, 210, 200],
        [210, 200, 207],
        [200, 207, 240],
        [207, 240, 269],
        [240, 269, 260],
        [269, 260, 263]]


def test_can_count_number_of_increases_over_windows():
    total_increases = count_window_set_increases()
    assert total_increases == 1418


def count_window_set_increases(readings=None, window_size=3):
    input = readings or get_readings()
    window_totals = sum_windows(window_size, input)
    return count_increases(window_totals)


def sum_windows(window_size, input):
    window_sets = windows(input, window_size)
    window_totals = (sum(window) for window in window_sets)
    return window_totals


def test_bar():
    input = read_file('course')
    zoo = list(x.split(' ') for x in input)
    down_total = sum(int(x[1]) for x in zoo if x[0] == 'down')
    up_total = sum(int(x[1]) for x in zoo if x[0] == 'up')
    depth = down_total - up_total
    forward_total = sum(int(x[1]) for x in zoo if x[0] == 'forward')

    # print(down_total)
    # print(up_total)
    # print(depth)
    # print(forward_total)
    # print(depth * forward_total)


def test_calc_aim():
    # input = [('forward', 5), ('down', 5), ('forward', 8),
    #          ('up', 3), ('down', 8), ('forward', 2)]
    file = read_file('course')
    input = list(x.split(' ') for x in file)
    aim = 0
    horiz = 0
    depth = 0
    for step in input:
        command = step[0]
        value = int(step[1])
        if(command == 'forward'):
            horiz += value
            depth += value * aim
        if(command == 'down'):
            aim += value
        if(command == 'up'):
            aim -= value
        if(aim < 0):
            print("*********************************")

    print(horiz)
    print(aim)
    print(depth)
    print(depth * horiz)
    # print(input)


def get_readings():
    return list(int(z) for z in read_file('input'))


def windows(input, window_size):
    return (input[i:i+window_size] for i in range(0, len(input) - window_size + 1))


def count_increases(data):
    prev = None
    count = 0
    for next in data:
        if(prev != None and next > prev):
            count += 1
        prev = next
    return count


def read_file(file):
    with open(file) as file:
        return [line.rstrip('\n') for line in file]
