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

chunk_open = ['[', '(', '{', '<']
chunk_close = [']', ')', '}', '>']
error_score = {')': 3, ']': 57, '}': 1197, '>': 25137}


def test_one():
    input = read_file('day10-input')
    corrupted_lines = find_corrupted_lines(input)

    scores = [error_score[x[1]] for x in corrupted_lines]
    total_score = sum(scores)
    print(scores)
    print(total_score)


def find_corrupted_lines(input):
    stack = []
    corrupted_lines = []
    for line in input:
        for char in line:
            if char in chunk_open:
                stack.append(char)
            if char in chunk_close:
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


def def_calc_completion_score():
    pass


def find_line_completion_chars(line):
    stack = []
    for char in line:
        if char in chunk_open:
            stack.append(char)
        if char in chunk_close:
            stack.pop()
    line_completion = [inverse_of_open(x) for x in stack]
    return line_completion


def inverse_of_close(char):
    index = chunk_close.index(char)
    return chunk_open[index]


def inverse_of_open(char):
    index = chunk_open.index(char)
    return chunk_close[index]
