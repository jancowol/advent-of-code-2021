import advent.day10 as d10
from advent.file_utils import read_file

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
                if(last_open_char != d10.inverse_of_close(char)):
                    corrupted_lines.append((line, char))
                    break
    return corrupted_lines


def test_two():
    print('---------------test 2')
    input = test_input
    corrupted_lines = [line[0] for line in find_corrupted_lines(input)]
    incomplete_lines = [x for x in input if x not in corrupted_lines]
    for line in incomplete_lines:
        line_completion = d10.find_line_completion_chars(line)
        print(line_completion)


def test_calc_completion_score():
    print('---------------')
    # ti = ['}', '}', ']', ']', ')', '}', ')', ']']

    input = read_file('day10-input')
    corrupted_lines = [line[0] for line in find_corrupted_lines(input)]
    incomplete_lines = [x for x in input if x not in corrupted_lines]

    totals = [d10.complete_and_score_line(x)[1] for x in incomplete_lines]
    sorted_totals = sorted(totals)
    mid_index = round(len(sorted_totals) / 2)
    print(sorted_totals[mid_index])

