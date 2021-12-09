import advent.day8 as d8

test_input = [
    'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe',
    'edbfga begcd cbg gc gcadebf fbgde acbgfd abcde gfcbed gfec | fcgedb cgb dgebacf gc    ',
    'fgaebd cg bdaec gdafb agbcfd gdcbef bgcad gfac gcb cdgabef | cg cg fdcagb cbg         ',
    'fbegcd cbd adcefb dageb afcb bc aefdc ecdab fgdeca fcdbega | efabcd cedba gadfec cb   ',
    'aecbfdg fbg gf bafeg dbefa fcge gcbea fcaegb dgceab fcbdga | gecf egdcabf bgf bfgea   ',
    'fgeab ca afcebg bdacfeg cfaedg gcfdb baec bfadeg bafgc acf | gebdcfa ecba ca fadegcb  ',
    'dbcfg fgd bdegcaf fgec aegbdf ecdfab fbedc dacgb gdcebf gf | cefg dcbef fcge gbcadfe  ',
    'bdfegc cbegaf gecbf dfcage bdacg ed bedf ced adcbefg gebcd | ed bcgafe cdgba cbgef    ',
    'egadfb cdbfeg cegd fecab cgb gbdefca cg fgcdab egfdb bfceg | gbdfcae bgc cg cgb       ',
    'gcafb gcf dcaebfg ecagb gf abcdeg gaef cafbge fdbac fegbdc | fgae cfgab fg bagce      ']


def test_can_count_unique_digits():
    lines = d8.parse_lines(test_input)
    unique_digit_count = d8.count_unique_output_digits(lines)
    assert unique_digit_count == 26


def test_part_2():
    print('*** part2')

    output_sum = 0
    test_input = 'be cfbegad cbdgef fgaecd cgeb fdcge agebfd fecdb fabcd edb | fdgacbe cefdb cefbgd gcbe'

    for x in d8.read_input():
        val = blahblahblah(x)
        output_sum += val
    # output_val = blahblahblah(parse_line(test_input))

    # output_sum += output_val
    print(output_sum)


def blahblahblah(xxx):
    # signals, output = parse_line(test_input)
    signals, output = xxx[0], xxx[1]
    signal_sets = [set(x) for x in signals]

    known_signal_set = {}
    one_signal = list([x for x in signal_sets if len(x) == 2])[0]
    known_signal_set.update({1: one_signal})
    four_signal = list([x for x in signal_sets if len(x) == 4])[0]
    known_signal_set.update({4: four_signal})
    seven_signal = list([x for x in signal_sets if len(x) == 3])[0]
    known_signal_set.update({7: seven_signal})
    eight_signal = list([x for x in signal_sets if len(x) == 7])[0]
    known_signal_set.update({8: eight_signal})

    numbers_with_6_segments = [x for x in signal_sets if len(x) == 6]
    nine_signal = list([x for x in numbers_with_6_segments if x.intersection(
        four_signal) == four_signal])[0]
    known_signal_set.update({9: nine_signal})

    segment_4 = list(eight_signal - nine_signal)[0]

    two_signal = [x for x in signal_sets if len(x) == 5 and segment_4 in x][0]
    known_signal_set.update({2: two_signal})

    # out of the set of 5 seg numbers, the one with seg == 1 after x - 2 is 3, and the one with seg == 2 after x - 2 is 5
    three_signal = [x for x in signal_sets if len(
        x) == 5 and len(x - two_signal) == 1][0]
    known_signal_set.update({3: three_signal})

    five_signal = [x for x in signal_sets if len(
        x) == 5 and len(x - two_signal) == 2][0]
    known_signal_set.update({5: five_signal})

    # in the set of 6 seg numbers without 9, x - 5 == 1 is 1s will be 6, and x - 5 == 2 will be 0
    zero_six_sets = [x for x in signal_sets if len(
        x) == 6 and x != nine_signal]
    zero_signal = [x for x in zero_six_sets if len(x - five_signal) == 2][0]
    known_signal_set.update({0: zero_signal})
    six_signal = [x for x in zero_six_sets if len(x - five_signal) == 1][0]
    known_signal_set.update({6: six_signal})

    output_sets = [set(x) for x in output]
    zzz = [str(bloop(known_signal_set, z)) for z in output_sets]
    output_val = int(''.join(zzz))
    return output_val


def bloop(known_signal_set, x):
    return [y[0] for y in known_signal_set.items() if y[1] == x][0]


def map_known_input_signals(signals, digit, seg_count):
    sig_for_digit = [x for x in signals if len(x) == seg_count][0]
    return {digit: set(sig_for_digit)}
