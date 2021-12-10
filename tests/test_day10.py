from advent.file_utils import read_file
from advent.day10 import *

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

    scores = [error_score[x[1]] for x in corrupted_lines]
    total_score = sum(scores)
    print(scores)
    print(total_score)


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
