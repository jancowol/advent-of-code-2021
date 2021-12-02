from src import advent


def test_can_read_file():
    data = advent.read_file('input')
    assert len(data) == 2000


def test_can_count_increases():
    data = [
        199,
        200,  # increase
        208,  # increase
        210,  # increase
        200,
        207,  # increase
        240,  # increase
        269,  # increase
        260,
        263,  # increase
    ]
    count = advent.count_increases(data)
    assert count == 7


def test_can_generate_windows():
    input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    window_groups = advent.windows(input, 3)
    assert list(window_groups) == [
        [199, 200, 208],
        [200, 208, 210],
        [208, 210, 200],
        [210, 200, 207],
        [200, 207, 240],
        [207, 240, 269],
        [240, 269, 260],
        [269, 260, 263]]


def test_can_sum_over_windows():
    input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    window_3_sums = advent.sum_windows(input, 3)
    assert list(window_3_sums) == [607, 618, 618, 617, 647, 716, 769, 792]

    window_4_sums = advent.sum_windows(input, 4)
    assert list(window_4_sums) == [817, 818, 825, 857, 916, 976, 1032]


def test_can_count_number_of_increases_over_windows():
    input = [199, 200, 208, 210, 200, 207, 240, 269, 260, 263]
    total_increases = advent.count_window_set_increases(input, 3)
    assert total_increases == 5


def test_bar():
    input = advent.read_file('course')
    boo = [(y[0], int(y[1])) for y in (x.split(' ') for x in input)]

    forward_total, down_total, up_total = aggregate_course_steps(boo)

    depth = down_total - up_total

    print(down_total)
    print(up_total)
    print(depth)
    print(forward_total)
    print(depth * forward_total)


def aggregate_course_steps(course_steps):
    forward_total = sum((x[1]) for x in course_steps if x[0] == 'forward')
    down_total = sum((x[1]) for x in course_steps if x[0] == 'down')
    up_total = sum((x[1]) for x in course_steps if x[0] == 'up')
    return forward_total, down_total, up_total


def test_calc_aim():
    # input = [('forward', 5), ('down', 5), ('forward', 8),
    #          ('up', 3), ('down', 8), ('forward', 2)]
    file = advent.read_file('course')
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
