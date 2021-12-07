import time
from advent import advent
from advent import bingoinput


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

    numbers4 = [93, 18, 74, 26, 98, 52, 94, 23, 15, 2, 34, 75, 13, 31, 39, 76, 96, 16, 84, 12, 38, 27, 8, 85, 86, 43, 4, 79, 57, 19, 40, 59, 14, 21, 35, 0, 90, 11, 32, 17, 78, 83, 54, 42, 66, 82, 99, 45,
                55, 63, 24, 5, 89, 46, 80, 49, 3, 48, 67, 47, 50, 60, 81, 51, 71, 33, 72, 6, 9, 30, 56, 20, 77, 29, 28, 69, 25, 36, 91, 92, 65, 22, 62, 58, 64, 88, 10, 7, 87, 41, 44, 37, 73, 70, 68, 97, 61, 95, 53, 1]
    day_4_1(numbers4)

    boards = bingoinput.boards
    for i in range(len(numbers4)):
        count = len(numbers4) - i
        nums = numbers4[:count]
        # print(nums)
        non_winning_boards = find_non_winning_boards(boards, nums)
        if(len(non_winning_boards) > 0):
            nwb = non_winning_boards[0]
            print(nwb)
            last_winning_board_numbers = numbers4[:count+1]
            unmarked_winning_board_numbers = unmarked_numbers_in_board(
                last_winning_board_numbers, nwb)
            unmarked_sum = sum(unmarked_winning_board_numbers)
            print(f'last winning board sum of unmared nums: {unmarked_sum}')
            # print(nums)
            last_num = last_winning_board_numbers[-1]
            print(f'last number in winning board seq: {last_num}')
            print(f'last winning board final answer {last_num * unmarked_sum}')
            # print(non_winning_boards)
            break


def day_4_1(drawn_numbers):
    winning_board, winning_number_set = find_winning_board(
        bingoinput.boards, drawn_numbers)
    unmarked_winning_board_numbers = unmarked_numbers_in_board(
        winning_number_set, winning_board)
    unmarked_sum = sum(unmarked_winning_board_numbers)
    print(f'winning board {winning_board}')
    print(f'board won at sequence {winning_number_set}')
    print(f'last number in winning set {winning_number_set[-1]}')
    print(f'unmarked winning board numbers {unmarked_winning_board_numbers}')
    print(f'sum of unmarked winning board numbers: {unmarked_sum}')
    print(f'final answer {unmarked_sum * winning_number_set[-1]}')


def find_winning_board(boards, numbers):
    for i in range(len(numbers)):
        nums = numbers[:i+1]
        winning_boards = find_winning_boards(boards, nums)
        if(len(winning_boards) > 0):
            return winning_boards[0], nums


def find_winning_boards(boards, numbers):
    return [board for board in boards if board_wins(board, numbers)]


def find_non_winning_boards(boards, numbers):
    return [board for board in boards if not board_wins(board, numbers)]


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


def test_can_calculate_horz_vert_line_points():
    horz_line = [(0, 9), (5, 9)]
    expected_line_points = [(0, 9), (1, 9), (2, 9), (3, 9), (4, 9), (5, 9)]
    h_line_points = horz_line_points(horz_line)
    assert h_line_points == expected_line_points

    horz_line2 = [(5, 9), (0, 9)]
    h_line_points2 = horz_line_points(horz_line2)
    assert h_line_points2 == expected_line_points

    vert_line = [(7, 0), (7, 4)]
    v_line_points = vert_line_points(vert_line)
    assert v_line_points == [(7, 0), (7, 1), (7, 2), (7, 3), (7, 4)]


def test_foo():
    input = read_day5_input()
    # break
    # print(input)
    # input = [
    #     [(0, 9), (5, 9)],
    #     [(8, 0), (0, 8)],
    #     [(9, 4), (3, 4)],
    #     [(2, 2), (2, 1)],
    #     [(7, 0), (7, 4)],
    #     [(6, 4), (2, 0)],
    #     [(0, 9), (2, 9)],
    #     [(3, 4), (1, 4)],
    #     [(0, 0), (8, 8)],
    #     [(5, 5), (8, 2)]]

    h_lines = [line for line in input if (
        line[0][0] != line[1][0]) and (line[0][1] == line[1][1])]
    h_line_points_sets = [horz_line_points(line) for line in h_lines]
    h_line_points = [
        point for pointset in h_line_points_sets for point in pointset]

    v_lines = [line for line in input if (
        line[0][1] != line[1][1]) and (line[0][0] == line[1][0])]
    v_line_points_sets = [vert_line_points(line) for line in v_lines]
    v_line_points = [
        point for pointset in v_line_points_sets for point in pointset]

    d_lines = [line for line in input if (
        line[0][1] != line[1][1]) and (line[0][0] != line[1][0])]
    d_line_points_sets = [diag_line_points(line) for line in d_lines]
    d_line_points = [
        point for pointset in d_line_points_sets for point in pointset]

    all_points = h_line_points + v_line_points + d_line_points
    blah = {}
    for point in all_points:
        count = blah.get(point, 0)
        blah.update({point: count + 1})
    fooz = [y for y in blah.items() if y[1] > 1]
    x = [f'{y}: {y[1]}' for y in fooz]

    # for y in x:
    #     print(y)

    print(f'overlapping points count: {len(fooz)}')


def vert_line_points(line):
    pt1, pt2 = line
    if(pt1[1] < pt2[1]):
        s = pt1[1]
        e = pt2[1]
    else:
        s = pt2[1]
        e = pt1[1]

    line_points = [(pt1[0], y) for y in range(s, e + 1)]
    return line_points


def diag_line_points(line):
    return get_line(line)
    # pt1, pt2 = line
    # if(pt1[1] < pt2[1]):
    #     s = pt1[1]
    #     e = pt2[1]
    # else:
    #     s = pt2[1]
    #     e = pt1[1]

    # line_points = [(pt1[0], y) for y in range(s, e + 1)]
    # return line_points


def horz_line_points(line):
    pt1, pt2 = line
    if(pt1[0] < pt2[0]):
        s = pt1[0]
        e = pt2[0]
    else:
        s = pt2[0]
        e = pt1[0]

    line_points = [(x, pt1[1]) for x in range(s, e + 1)]
    return line_points


def read_day5_input():
    file_data = advent.read_file('day5-input')
    foo = [split_foo(y) for y in [x.split('->') for x in file_data]]
    # print(foo)
    # bar = [(y[0].split(','), y[1].split(',')) for y in foo]
    # print(bar)
    return foo


def split_foo(y):
    bar = y[0].strip(), y[1].strip()
    fooz = bar[0].split(','), bar[1].split(',')
    return [(int(fooz[0][0]), int(fooz[0][1])), (int(fooz[1][0]), int(fooz[1][1]))]


def test_get_points():
    pass
    print(get_line([(0, 6), (6, 0)]))


def get_line(line):
    x1 = line[0][0]
    y1 = line[0][1]
    x2 = line[1][0]
    y2 = line[1][1]
    points = []
    issteep = abs(y2-y1) > abs(x2-x1)
    if issteep:
        x1, y1 = y1, x1
        x2, y2 = y2, x2
    rev = False
    if x1 > x2:
        x1, x2 = x2, x1
        y1, y2 = y2, y1
        rev = True
    deltax = x2 - x1
    deltay = abs(y2-y1)
    error = int(deltax / 2)
    y = y1
    ystep = None
    if y1 < y2:
        ystep = 1
    else:
        ystep = -1
    for x in range(x1, x2 + 1):
        if issteep:
            points.append((y, x))
        else:
            points.append((x, y))
        error -= deltay
        if error < 0:
            y += ystep
            error += deltax
    # Reverse the list if the coordinates were reversed
    if rev:
        points.reverse()
    return points


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


def test_day_6_1_model_fish_internal_clock():
    f = Fish(3)

    f.day_tick()
    assert f.clock == 2

    f.day_tick()
    assert f.clock == 1

    result = f.day_tick()
    assert f.clock == 0
    assert result == None

    result = f.day_tick()
    assert f.clock == 6
    assert result == 8


def test_day_6_1_model_fish_school():
    fish_clocks = [3, 4, 3, 1, 2]
    expected_after_18_days = [6, 0, 6, 4, 5, 6, 0, 1, 1,
                              2, 6, 0, 1, 1, 1, 2, 2, 3, 3, 4, 6, 7, 8, 8, 8, 8]

    school = [Fish(clock) for clock in fish_clocks]

    result_school = model_school_spawn(school, 18)

    end_fish_clocks = [f.clock for f in result_school]
    assert end_fish_clocks == expected_after_18_days


def test_against_advent_example():
    fish_clocks = [3, 4, 3, 1, 2]

    result_school = model_school_from_clocks(fish_clocks, 80)

    assert len(result_school) == 5934


def model_school_from_clocks(fish_clocks, days):
    school = [Fish(clock) for clock in fish_clocks]
    return model_school_spawn(school, days)

# def test_solve_day_6_1():
#     puzzle_input = [1,1,3,5,1,3,2,1,5,3,1,4,4,4,1,1,1,3,1,4,3,1,2,2,2,4,1,1,5,5,4,3,1,1,1,1,1,1,3,4,1,2,2,5,1,3,5,1,3,2,5,2,2,4,1,1,1,4,3,3,3,1,1,1,1,3,1,3,3,4,4,1,1,5,4,2,2,5,4,5,2,5,1,4,2,1,5,5,5,4,3,1,1,4,1,1,3,1,3,4,1,1,2,4,2,1,1,2,3,1,1,1,4,1,3,5,5,5,5,1,2,2,1,3,1,2,5,1,4,4,5,5,4,1,1,3,3,1,5,1,1,4,1,3,3,2,4,2,4,1,5,5,1,2,5,1,5,4,3,1,1,1,5,4,1,1,4,1,2,3,1,3,5,1,1,1,2,4,5,5,5,4,1,4,1,4,1,1,1,1,1,5,2,1,1,1,1,2,3,1,4,5,5,2,4,1,5,1,3,1,4,1,1,1,4,2,3,2,3,1,5,2,1,1,4,2,1,1,5,1,4,1,1,5,5,4,3,5,1,4,3,4,4,5,1,1,1,2,1,1,2,1,1,3,2,4,5,3,5,1,2,2,2,5,1,2,5,3,5,1,1,4,5,2,1,4,1,5,2,1,1,2,5,4,1,3,5,3,1,1,3,1,4,4,2,2,4,3,1,1]
#     result = model_school_from_clocks(puzzle_input, 80)
#     print(f'***** day 6.1 {len(result)}')

# def test_solve_day_6_2():
#     puzzle_input = [1,1,3,5,1,3,2,1,5,3,1,4,4,4,1,1,1,3,1,4,3,1,2,2,2,4,1,1,5,5,4,3,1,1,1,1,1,1,3,4,1,2,2,5,1,3,5,1,3,2,5,2,2,4,1,1,1,4,3,3,3,1,1,1,1,3,1,3,3,4,4,1,1,5,4,2,2,5,4,5,2,5,1,4,2,1,5,5,5,4,3,1,1,4,1,1,3,1,3,4,1,1,2,4,2,1,1,2,3,1,1,1,4,1,3,5,5,5,5,1,2,2,1,3,1,2,5,1,4,4,5,5,4,1,1,3,3,1,5,1,1,4,1,3,3,2,4,2,4,1,5,5,1,2,5,1,5,4,3,1,1,1,5,4,1,1,4,1,2,3,1,3,5,1,1,1,2,4,5,5,5,4,1,4,1,4,1,1,1,1,1,5,2,1,1,1,1,2,3,1,4,5,5,2,4,1,5,1,3,1,4,1,1,1,4,2,3,2,3,1,5,2,1,1,4,2,1,1,5,1,4,1,1,5,5,4,3,5,1,4,3,4,4,5,1,1,1,2,1,1,2,1,1,3,2,4,5,3,5,1,2,2,2,5,1,2,5,3,5,1,1,4,5,2,1,4,1,5,2,1,1,2,5,4,1,3,5,3,1,1,3,1,4,4,2,2,4,3,1,1]
#     result = model_school_from_clocks(puzzle_input, 256)
#     print(f'***** day 6.2 {len(result)}')


def test_solve_day_6_2_approach2():
    input = [1, 1, 3, 5, 1, 3, 2, 1, 5, 3, 1, 4, 4, 4, 1, 1, 1, 3, 1, 4, 3, 1, 2, 2, 2, 4, 1, 1, 5, 5, 4, 3, 1, 1, 1, 1, 1, 1, 3, 4, 1, 2, 2, 5, 1, 3, 5, 1, 3, 2, 5, 2, 2, 4, 1, 1, 1, 4, 3, 3, 3, 1, 1, 1, 1, 3, 1, 3, 3, 4, 4, 1, 1, 5, 4, 2, 2, 5, 4, 5, 2, 5, 1, 4, 2, 1, 5, 5, 5, 4, 3, 1, 1, 4, 1, 1, 3, 1, 3, 4, 1, 1, 2, 4, 2, 1, 1, 2, 3, 1, 1, 1, 4, 1, 3, 5, 5, 5, 5, 1, 2, 2, 1, 3, 1, 2, 5, 1, 4, 4, 5, 5, 4, 1, 1, 3, 3, 1, 5, 1, 1, 4, 1, 3, 3, 2, 4, 2, 4,
             1, 5, 5, 1, 2, 5, 1, 5, 4, 3, 1, 1, 1, 5, 4, 1, 1, 4, 1, 2, 3, 1, 3, 5, 1, 1, 1, 2, 4, 5, 5, 5, 4, 1, 4, 1, 4, 1, 1, 1, 1, 1, 5, 2, 1, 1, 1, 1, 2, 3, 1, 4, 5, 5, 2, 4, 1, 5, 1, 3, 1, 4, 1, 1, 1, 4, 2, 3, 2, 3, 1, 5, 2, 1, 1, 4, 2, 1, 1, 5, 1, 4, 1, 1, 5, 5, 4, 3, 5, 1, 4, 3, 4, 4, 5, 1, 1, 1, 2, 1, 1, 2, 1, 1, 3, 2, 4, 5, 3, 5, 1, 2, 2, 2, 5, 1, 2, 5, 3, 5, 1, 1, 4, 5, 2, 1, 4, 1, 5, 2, 1, 1, 2, 5, 4, 1, 3, 5, 3, 1, 1, 3, 1, 4, 4, 2, 2, 4, 3, 1, 1]

    def timed_test():
        result = count_many_generations(input)
        print(result)
        assert result == 1631629590423

    timed(timed_test)


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


def timed(func):
    start = time.time()
    func()
    end = time.time()
    print((end - start) * 1000)


def model_school_spawn(initial_school, simulation_days):
    school = initial_school
    for i in range(simulation_days):
        new_fish = [Fish(new_fish_age) for new_fish_age in (
            foo.day_tick() for foo in school) if new_fish_age != None]
        school += new_fish
    return school

# 1,631,629,590,423
