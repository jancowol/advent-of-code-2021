from src import advent
from src import bingoinput


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


def test_day4_1():
    numbers3 = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10,
                16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]

    board1 = [
        [22, 13, 17, 11,  0, ],
        [8,  2,  23,  4, 24, ],
        [21,  9, 14, 16,  7, ],
        [6, 10,  3, 18,  5, ],
        [1, 12,  20, 15, 19, ]]

    board2 = [
        [3, 15,  0,  2, 22, ],
        [9, 18, 13, 17,  5, ],
        [19,  8,  7, 25, 23, ],
        [20, 11, 10, 24,  4, ],
        [14, 21, 16, 12,  6, ]]

    board3 = [
        [14, 21, 17, 24,  4, ],
        [10, 16, 15,  9, 19, ],
        [18,  8, 23, 26, 20, ],
        [22, 11, 13,  6,  5, ],
        [2,  0,  12,  3,  7, ]]

    numbers = {20, 199, 11, 10, 299, 24,  4, }  # should match row 4 on board2
    assert board_row_contains_all(numbers, board1) == False
    assert board_row_contains_all(numbers, board2) == True
    assert board_row_contains_all(numbers, board3) == False

    # should match column 3 on board 1
    numbers2 = {17, 23, 1999, 14, 3, 2999, 20}
    assert board_col_contains_all(board1, numbers2) == True
    assert board_col_contains_all(board2, numbers2) == False
    assert board_col_contains_all(board3, numbers2) == False

    numbers3 = {7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24}
    assert board_wins(board1, numbers3) == False
    assert board_wins(board2, numbers3) == False
    assert board_wins(board3, numbers3) == True

    unmarked_board_numbers = unmarked_numbers_in_board(numbers3, board3)
    unmarked_num_sum = sum(unmarked_board_numbers)

    print(unmarked_board_numbers)
    print(unmarked_num_sum)
    print(unmarked_num_sum * 24)

    numbers4 = [7, 4, 9, 5, 11, 17, 23, 2, 0, 14, 21, 24, 10,
                16, 13, 6, 15, 25, 12, 22, 18, 20, 8, 19, 3, 26, 1]
    evaluate_board_num_input(board3, numbers4)

def evaluate_board_num_input(board, numbers):
    for i in range(len(numbers)):
        nums = numbers[:i+1]
        print(nums)
        if(board_wins(board, nums)):
            print('board 3 wins')
            last_num = nums[-1]
            print(f'last no. is {last_num}')
            break
        else:
            print('no win')


def unmarked_numbers_in_board(marked, board):
    flat_board = [number for row in board for number in row]
    unmarked = set(flat_board).difference(marked)
    return unmarked


def board_wins(board, numbers):
    return board_row_contains_all(numbers, board) or board_col_contains_all(board, numbers)


def board_col_contains_all(board, numbers):
    for i in range(len(board[0])):
        col = [row[i] for row in board]
        if(set(col).issubset(numbers)):
            return True
    return False


def board_row_contains_all(numbers, board):
    for row in board:
        r2 = set(row)
        if(r2.issubset(numbers)):
            return True
    return False
