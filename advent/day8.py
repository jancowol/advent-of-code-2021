import advent as advent


def find_unique_segment_digits(input):
    return [digit_segments for digit_segments in input if is_unique_segment_count(digit_segments)]


def is_unique_segment_count(segment_count):
    return len(segment_count) in [2, 3, 4, 7]


def parse_lines(input):
    return [parse_line(line) for line in input]


def read_input():
    result = advent.read_file('day8-input')
    return [parse_line(x) for x in result]


def parse_line(x):
    line_parts = x.split('|')
    signals = line_parts[0].strip()
    sig_parts = signals.split(' ')
    output = line_parts[1].strip()
    output_parts = output.split(' ')
    return (sig_parts, output_parts)


def count_unique_output_digits(lines):
    unique_digits = [find_unique_segment_digits(x[1]) for x in lines]
    unique_digit_count = sum([len(x) for x in unique_digits])
    return unique_digit_count


print('***** Day 8 *****')
input = read_input()
unique_digit_count = count_unique_output_digits(input)
print(f'Number of unique digits in output {unique_digit_count}')
