
def read_file(file):
    with open(file) as file:
        return [line.rstrip('\n') for line in file]