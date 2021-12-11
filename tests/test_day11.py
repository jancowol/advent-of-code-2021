from dataclasses import dataclass
from itertools import *

input = [
    '1553421288',
    '5255384882',
    '1224315732',
    '4258242274',
    '1658564216',
    '6872651182',
    '5775552238',
    '5622545172',
    '8766672318',
    '2178374835',
]

test_input = [
    '5483143223',
    '2745854711',
    '5264556173',
    '6141336146',
    '6357385478',
    '4167524645',
    '2176841721',
    '6882881134',
    '4846848554',
    '5283751526',
]


@dataclass
class Point:
    x: int
    y: int
    x_limit: int = 9
    y_limit: int = 9

    def __hash__(self):
        return hash(str(self))

    def unlimited_adjacents(self):
        adj = [
            Point(self.x - 1, self.y - 1, self.x_limit, self.y_limit),
            Point(self.x, self.y - 1, self.x_limit, self.y_limit),
            Point(self.x + 1, self.y - 1, self.x_limit, self.y_limit),
            Point(self.x - 1, self.y, self.x_limit, self.y_limit),
            Point(self.x + 1, self.y, self.x_limit, self.y_limit),
            Point(self.x - 1, self.y + 1, self.x_limit, self.y_limit),
            Point(self.x, self.y + 1, self.x_limit, self.y_limit),
            Point(self.x + 1, self.y + 1, self.x_limit, self.y_limit)]

        return adj

    def adjacents(self):
        return [p for p in self.unlimited_adjacents() if p.x >= 0 and p.y >= 0 and p.x <= self.x_limit and p.y <= self.y_limit]


def flat_map(f, xs): return (y for ys in xs for y in f(ys))


def flash_step(input, increase_at_pos, already_flashed):
    if(already_flashed == None):
        already_flashed = set()
    if(len(increase_at_pos) == 0):
        return
    increase_energy(input, increase_at_pos)
    flashes = [pos_energy[0] for pos_energy in input.items(
    ) if pos_energy[1] > 9 and pos_energy[0] not in already_flashed]
    already_flashed.update(flashes)

    adjacents = [x.adjacents() for x in flashes]
    flat_adjacents = flat_map(lambda x: x, adjacents)
    non_flashed_adjacents = [
        x for x in flat_adjacents if x not in already_flashed]
    flash_step(input, non_flashed_adjacents, already_flashed)

    return len(already_flashed)


def build_energy_map(input):
    energy_map = {}
    for y in range(10):
        for x in range(10):
            energy = int(input[y][x])
            energy_map[Point(x, y)] = energy

    return energy_map


def test_one():
    energy_map = build_energy_map(test_input)

    flash_counts = [tick(energy_map) for x in range(100)]
    total_flashes = sum(flash_counts)
    assert total_flashes == 1656


def test_two():
    energy_map = build_energy_map(test_input)
    for i in range(1, 1000):
        flash_counts = tick(energy_map)
        if(flash_counts == 100):
            print(f'all flashed at iteration {i}')
            break


def tick(energy_by_pos):
    flash_count = flash_step(energy_by_pos, energy_by_pos.keys(), set())
    for x in [y[0] for y in energy_by_pos.items() if y[1] > 9]:
        energy_by_pos[x] = 0
    return flash_count


def increase_energy(energy_states, increase_at_pos):
    for item in increase_at_pos:
        energy_states[item] += 1