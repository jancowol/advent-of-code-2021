import advent.day10 as d10
from advent.file_utils import read_file
from functools import reduce

test_input = [
    '[({(<(())[]>[[{[]{<()<>>',
    '[(()[<>])]({[<{<<[]>>(',
    '{([(<{}[<>[]}>{[]{[(<()>',
    '(((({<>}<{<{<>}{[]{[]{}',
    '[[<[([]))<([[{}[[()]]]',
    '[{[{({}]{}}([{[{{{}}([]',
    '{<[[]]>}<{[{[{[]{()[[[]',
    '[<(<(<(<{}))><([]([]()',
    '<{([([[(<>()){}]>(<<{{',
    '<{([{{}}[<[[[<>{}]]]>[]]']


def test_one():
    input = read_file('day10-input')
    corrupted_lines = find_corrupted_lines(input)

    scores = [d10.error_score[x[1]] for x in corrupted_lines]
    total_score = sum(scores)
    print(scores)
    print(total_score)


def find_corrupted_lines(input):
    stack = []
    corrupted_lines = []
    for line in input:
        for char in line:
            if char in d10.chunk_open:
                stack.append(char)
            if char in d10.chunk_close:
                last_open_char = stack.pop()
                if(last_open_char != inverse_of_close(char)):
                    corrupted_lines.append((line, char))
                    break
    return corrupted_lines


def test_two():
    print('---------------test 2')
    input = test_input
    corrupted_lines = [line[0] for line in find_corrupted_lines(input)]
    incomplete_lines = [x for x in input if x not in corrupted_lines]
    for line in incomplete_lines:
        line_completion = find_line_completion_chars(line)
        print(line_completion)


def test_calc_completion_score():
    print('---------------')
    # ti = ['}', '}', ']', ']', ')', '}', ')', ']']

    input = read_file('day10-input')
    corrupted_lines = [line[0] for line in find_corrupted_lines(input)]
    incomplete_lines = [x for x in input if x not in corrupted_lines]

    totals = [complete_and_score_line(x)[1] for x in incomplete_lines]
    sorted_totals = sorted(totals)
    mid_index = round(len(sorted_totals) / 2)
    print(sorted_totals[mid_index])


def complete_and_score_line(line):
    line_completion = find_line_completion_chars(line)
    completion_score = calc_completion_score(line_completion)
    return line_completion, completion_score


def calc_completion_score(test_input):
    points = [d10.points_lookup[x] for x in test_input]
    total = reduce(lambda x, y: (x*5) + y, points, 0)
    return total


def find_line_completion_chars(line):
    stack = []
    for char in line:
        if char in d10.chunk_open:
            stack.append(char)
        if char in d10.chunk_close:
            stack.pop()
    line_completion = [inverse_of_open(x) for x in reversed(stack)]
    return line_completion


def inverse_of_close(char):
    index = d10.chunk_close.index(char)
    return d10.chunk_open[index]


def inverse_of_open(char):
    index = d10.chunk_open.index(char)
    return d10.chunk_close[index]
