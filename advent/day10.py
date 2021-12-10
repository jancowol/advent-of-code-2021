from functools import reduce

chunk_open = ['[', '(', '{', '<']
chunk_close = [']', ')', '}', '>']
error_score = {')': 3, ']': 57, '}': 1197, '>': 25137}
points_lookup = {')': 1, ']': 2, '}': 3, '>': 4}

def complete_and_score_line(line):
    line_completion = find_line_completion_chars(line)
    completion_score = calc_completion_score(line_completion)
    return line_completion, completion_score


def calc_completion_score(test_input):
    points = [points_lookup[x] for x in test_input]
    total = reduce(lambda x, y: (x*5) + y, points, 0)
    return total


def find_line_completion_chars(line):
    stack = []
    for char in line:
        if char in chunk_open:
            stack.append(char)
        if char in chunk_close:
            stack.pop()
    line_completion = [inverse_of_open(x) for x in reversed(stack)]
    return line_completion


def inverse_of_close(char):
    index = chunk_close.index(char)
    return chunk_open[index]


def inverse_of_open(char):
    index = chunk_open.index(char)
    return chunk_close[index]