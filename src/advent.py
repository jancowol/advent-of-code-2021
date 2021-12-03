from dataclasses import dataclass


def read_file(file):
    with open(file) as file:
        return [line.rstrip('\n') for line in file]


def count_increases(data):
    prev = None
    count = 0
    for next in data:
        if(prev != None and next > prev):
            count += 1
        prev = next
    return count


def windows(input, window_size):
    return (input[i:i+window_size] for i in range(0, len(input) - window_size + 1))


def get_readings():
    return list(int(z) for z in read_file('input'))


def sum_windows(data, window_size):
    window_sets = windows(data, window_size)
    window_totals = (sum(window) for window in window_sets)
    return window_totals


def count_window_set_increases(readings=None, window_size=3):
    input = readings or get_readings()
    window_totals = sum_windows(input, window_size)
    return count_increases(window_totals)


@dataclass
class CourseStep:
    direction: str
    value: int


def parse_course_data(input):
    return [CourseStep(step[0], int(step[1])) for step in
            (raw_step.split(' ') for raw_step in input)]


def aggregate_course_steps(course_steps):
    # 3 * O(n) operations, could reduce to a single O(n) op using mutable approach
    forward_total = sum(
        step.value for step in course_steps if step.direction == 'forward')

    down_total = sum(
        step.value for step in course_steps if step.direction == 'down')

    up_total = sum(
        step.value for step in course_steps if step.direction == 'up')

    return forward_total, down_total, up_total


def day_2_1():
    input = read_file('course')
    course_steps = parse_course_data(input)
    forward_total, down_total, up_total = aggregate_course_steps(
        course_steps)

    depth = down_total - up_total

    print(down_total)
    print(up_total)
    print(depth)
    print(forward_total)
    print(depth * forward_total)


def day_2_2():
    file = read_file('course')
    course_steps = parse_course_data(file)
    aim, horiz, depth = calculate_with_aim(course_steps)

    print(f'horizontal: {horiz}')
    print(f'aim: {aim}')
    print(f'depth: {depth}')
    print(f'calc: {depth * horiz}')


def calculate_with_aim(course_steps):
    aim = 0
    horiz = 0
    depth = 0
    for step in course_steps:
        if(step.direction == 'forward'):
            horiz += step.value
            depth += step.value * aim
        if(step.direction == 'down'):
            aim += step.value
        if(step.direction == 'up'):
            aim -= step.value

    return aim, horiz, depth


def calc_co2_scrubber(data, bit_index=0):
    if(len(data) == 1):
        return data[0]
    filtered = filter_co2_scrubber(data, bit_index)
    return calc_co2_scrubber(filtered, bit_index + 1)


def filter_co2_scrubber(data, bit_index):
    oncount, offcount = count_bits(data, bit_index)
    least = '1' if oncount < offcount else '0'
    return [x for x in data if x[bit_index] == least]


def calc_oxygen_gen_rating(filtered, bits):
    for index in range(bits):
        filtered = filter_oxy(filtered, index)
    return filtered[0]


def filter_oxy(data, bit_index):
    boot = bit_index
    oncount, offcount = count_bits(data, bit_index)
    dominant = '1' if oncount >= offcount else '0'
    filtered = [x for x in data if x[boot] == dominant]
    return filtered


def count_bits(data, bit_index):
    oncount = 0
    offcount = 0
    for reading in data:
        if(reading[bit_index] == '1'):
            oncount += 1
        else:
            offcount += 1
    return oncount, offcount


def day_3_2():
    data = read_file('diagnostic')

    oxy_rating = calc_oxygen_gen_rating(data, 12)
    oxy_int = int(oxy_rating, 2)

    co2_scrubber = calc_co2_scrubber(data)
    co2_int = int(co2_scrubber, 2)

    print(f'Oxygen generator rating: {oxy_int}')
    print(f'CO2 Scrubber rating: {co2_int}')
    print(f'Life support rating: {oxy_int * co2_int}')


print('============= Day 2, part 1 =============')
day_2_1()

print('============= Day 2, part 2 =============')
day_2_2()

print('============= Day 3, part 2 =============')
day_3_2()
