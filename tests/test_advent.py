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

    bit_counts = [index_slice(data, i) for i in range(5)]

    gamma = zoot(bit_counts, '1', '0')
    assert gamma == 22

    epsilon = zoot(bit_counts, '0', '1')
    assert epsilon == 9

    power_cons = gamma * epsilon
    assert power_cons == 198


def index_slice(data, bit_index):
    slice = [int(reading[bit_index]) for reading in data]
    oncount = sum(slice)
    offcount = len(slice) - oncount
    return oncount, offcount


# def calculate_power_consumption():
#     file = advent.read_file('diagnostic')
#     data = file
#     foo1(data)


def zoot(bit_counts, boo, koo):
    bits = [boo if x[0] > x[1] else koo for x in bit_counts]
    int_of_bits = int(''.join(bits), 2)
    return int_of_bits


def test_calc_oxygen_generator_rating():
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

    oxy_rating = advent.calc_oxygen_gen_rating(data)
    assert oxy_rating == '10111'


def test_calc_co2_scrubber():
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
    result = advent.calc_co2_scrubber(data, 0)
    assert result == '01010'


def test_count_bits():
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
    assert advent.count_bits(data, 0) == (7, 5)
    assert advent.count_bits(data, 1) == (5, 7)
    assert advent.count_bits(data, 2) == (8, 4)
    assert advent.count_bits(data, 3) == (7, 5)
    assert advent.count_bits(data, 4) == (5, 7)
