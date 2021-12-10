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
    '<{([(( [(<>()){}]>(<<{{',
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
    incomplete_lines = find_incomplete_lines(input)
    for line in incomplete_lines:
        line_completion = find_line_completion_chars(line)
        print(line_completion)


def test_calc_completion_score():
    input = read_file('day10-input')
    best_score = calc_best_autocomplete_score(input)
    assert best_score == 3646451424
