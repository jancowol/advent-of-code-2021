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
    pass


def inverse_of_close(char):
    index = chunk_close.index(char)
    return chunk_open[index]
