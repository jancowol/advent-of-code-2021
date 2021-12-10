from functools import reduce

chunk_open = ['[', '(', '{', '<']
chunk_close = [']', ')', '}', '>']
error_score = {')': 3, ']': 57, '}': 1197, '>': 25137}
points_lookup = {')': 1, ']': 2, '}': 3, '>': 4}


def find_incomplete_lines(input):
    corrupt_lines = [line for line in input if line_is_corrupt(line)]
    incomplete_lines = (line for line in input if line not in corrupt_lines)
    return incomplete_lines


def find_corrupted_lines(input):
    corrupted_lines = []
    for line in input:
        invalid_char = line_is_corrupt(line)
        if(invalid_char):
            corrupted_lines.append((line, invalid_char))
    return corrupted_lines


def line_is_corrupt(line):
    first_invalid_char = find_first_invalid_char(line)
    if(first_invalid_char != None):
        return first_invalid_char


def find_first_invalid_char(line):
    stack = []
    for char in line:
        if char in chunk_open:
            stack.append(char)
        if char in chunk_close:
            last_open_char = stack.pop()
            if(last_open_char != inverse_of(char)):
                return char


def complete_and_score_line(line):
    line_completion = find_line_completion_chars(line)
    completion_score = calc_completion_score(line_completion)
    return completion_score


def calc_completion_score(completion):
    points = [points_lookup[char] for char in completion]
    total = reduce(lambda x, y: (x*5) + y, points, 0)
    return total


def find_line_completion_chars(line):
    stack = []
    for char in line:
        if char in chunk_open:
            stack.append(char)
        if char in chunk_close:
            stack.pop()
    line_completion = [inverse_of(x) for x in reversed(stack)]
    return line_completion


def inverse_of(char):
    if(char in chunk_close):
        return chunk_open[chunk_close.index(char)]
    else:
        return chunk_close[chunk_open.index(char)]


def calc_best_autocomplete_score(input):
    incomplete_lines = find_incomplete_lines(input)
    totals = (complete_and_score_line(line) for line in incomplete_lines)
    sorted_totals = sorted(totals)
    mid_index = round(len(sorted_totals) / 2)
    best_score = sorted_totals[mid_index]

    return best_score
