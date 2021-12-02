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
