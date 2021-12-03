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


def test_course_step_aggregation():
    data = [
        advent.CourseStep('forward', 5),
        advent.CourseStep('down', 5),
        advent.CourseStep('forward', 8),
        advent.CourseStep('up', 3),
        advent.CourseStep('down', 8),
        advent.CourseStep('forward', 2),
        advent.CourseStep('up', 13),
    ]

    forward_total, down_total, up_total = advent.aggregate_course_steps(data)
    assert forward_total == 15
    assert down_total == 13
    assert up_total == 16


def test_calc_aim():
    data = [
        advent.CourseStep('forward', 5),
        advent.CourseStep('down', 5),
        advent.CourseStep('forward', 8),
        advent.CourseStep('up', 3),
        advent.CourseStep('down', 8),
        advent.CourseStep('forward', 2),
        advent.CourseStep('up', 1),
        advent.CourseStep('forward', 1),
    ]
    aim, horiz, depth = advent.calculate_with_aim(data)
    assert aim == 9
    assert horiz == 16
    assert depth == 69


def test_power_consumption():
    data = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010',
    ]
    file = advent.read_file('diagnostic')
    data = file
    # print(file)
    oncounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    offcounts = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for foo in data:
        next = 0
        for boo in foo:
            if(boo == '1'):
                oncounts[next] += 1
            if(boo == '0'):
                offcounts[next] += 1
            next += 1
    print(oncounts)
    print(offcounts)
    gamma = ''
    epsilon = ''
    for zoo in range(12):
        if(oncounts[zoo] > offcounts[zoo]):
            gamma += '1'
            epsilon += '0'
        else:
            gamma += '0'
            epsilon += '1'
    gamma_int = int(gamma, 2)
    print(f'gamma: {gamma}')
    print(f'gamma int: {gamma_int}')

    epsilon_int = int(epsilon, 2)
    print(f'epsilon: {epsilon}')
    print(f'epsilon: {epsilon_int}')

    power_cons = gamma_int * epsilon_int
    print(f'power cons: {power_cons}')


def test_life_support_rating():
    data = [
        '00100',
        '11110',
        '10110',
        '10111',
        '10101',
        '01111',
        '00111',
        '11100',
        '10000',
        '11001',
        '00010',
        '01010',
    ]

    oxy_rating = calc_oxygen_gen_rating(data, 5)
    assert oxy_rating == '10111'

    result = calc_co2_scrubber(data, 5)
    assert result == '01010'

def test_calc_real_life_support():
    data = advent.read_file('diagnostic')

    oxy_rating = calc_oxygen_gen_rating(data, 12)
    print(oxy_rating)
    oxy_int = int(oxy_rating, 2)
    print(oxy_int)

    co2_scrubber = calc_co2_scrubber(data, 12)
    print(co2_scrubber)
    co2_int = int(co2_scrubber, 2)
    print(co2_int)

    print(oxy_int * co2_int)

def calc_co2_scrubber(data, bit_count):
    for index in range(bit_count):
        data = filter_co2_scrubber(data, index)
        if(len(data) == 1):
            break
    return data[0]


def filter_co2_scrubber(data, bit_index):
    oncount, offcount = count_bits(data, bit_index)
    least = '1' if oncount < offcount else '0'
    return [x for x in data if x[bit_index] == least]


def calc_oxygen_gen_rating(filtered, bits):
    for index in range(bits):
        filtered = filter_oxy(filtered, index)
    return filtered[0]


def filter_oxy(data, bit_index):
    boot = bit_index
    oncount, offcount = count_bits(data, bit_index)
    dominant = '1' if oncount >= offcount else '0'
    filtered = [x for x in data if x[boot] == dominant]
    return filtered


def count_bits(data, bit_index):
    oncount = 0
    offcount = 0
    for reading in data:
        if(reading[bit_index] == '1'):
            oncount += 1
        else:
            offcount += 1
    return oncount, offcount
