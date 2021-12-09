from dataclasses import dataclass
from advent.file_utils import read_file
from functools import reduce

test_input = [
    '2199943210',
    '3987894921',
    '9856789892',
    '8767896789',
    '9899965678',
]


@dataclass
class Point:
    x: int
    y: int
    x_limit: int = 99
    y_limit: int = 99

    def __hash__(self):
        return hash(str(self))

    def unlimited_adjacents(self):
        adj = [Point(self.x, self.y - 1, self.x_limit, self.y_limit), Point(self.x - 1, self.y, self.x_limit, self.y_limit),
               Point(self.x + 1, self.y, self.x_limit, self.y_limit), Point(self.x, self.y + 1, self.x_limit, self.y_limit)]

        return adj

    def adjacents(self):
        return [p for p in self.unlimited_adjacents() if p.x >= 0 and p.y >= 0 and p.x <= self.x_limit and p.y <= self.y_limit]


def test_find_adjacents_not_at_edge():
    point = Point(1, 1)
    expected_adjacents = set([
        Point(1, 0),
        Point(0, 1),
        Point(2, 1),
        Point(1, 2)])

    assert set(point.unlimited_adjacents()) == expected_adjacents


def test_can_filter_adjacents_to_map_limits():
    x_limit = len(test_input[0]) - 1
    y_limit = len(test_input) - 1

    point = Point(0, 0, x_limit, y_limit)
    expected_adjacents = set([
        Point(1, 0, x_limit, y_limit),
        Point(0, 1, x_limit, y_limit)])

    adjacents = set(point.adjacents())
    assert adjacents == expected_adjacents


def test_map_build():
    x_limit = len(test_input[0]) - 1
    y_limit = len(test_input) - 1
    m4 = build_map(test_input, x_limit, y_limit)
    print('******************* map building')
    print(m4)


def test_can_find_low_points():
    map = build_map(test_input, 9, 4)
    result = sum_low_point_risks(map)
    assert result == 15


def test_actual_data():
    input = read_file('day9-input')
    map = build_map(input)
    result = sum_low_point_risks(map)
    print(result)


def test_basins():
    input = read_file('day9-input')
    x_limit = len(input[0]) - 1
    y_limit = len(input) - 1
    map = build_map(input, x_limit, y_limit)
    low_points = find_low_points(map)

    print('****************')
    basins = [compute_basin(x, set([x]), x_limit, y_limit, map)
              for x in low_points]
    basin_sizes = sorted([len(basin) for basin in basins], reverse=True)[:3]
    print(basin_sizes)
    foo = reduce(lambda x, y: x * y, basin_sizes)
    print(foo)


def compute_basin(point: Point, basin, x_limit, y_limit, map):
    adjacent_points = point.adjacents()

    exp = set([x for x in adjacent_points if map[x] <
              9 and map[x] > map[point]]) - basin

    if(len(exp) == 0):
        return basin

    n = set(exp)
    for pt in exp:
        next_basin_points = compute_basin(pt, basin, x_limit, y_limit, map)
        n.update(next_basin_points)

    return n


def sum_low_point_risks(map):
    low_points = find_low_points(map)
    heights = [map[point] for point in low_points]
    risk_scores = [x + 1 for x in heights]
    result = sum(risk_scores)
    return result


def find_low_points(map):
    low_points = [
        point for point in map
        if map[point] < min([map[foo] for foo in point.adjacents()])]

    return low_points


def build_map(input, x_limit=99, y_limit=99):
    row_reading_count = len(input[0])
    map = list(zip(range(row_reading_count), [reading for reading in input]))
    m2 = [([(Point(x[0], row[0], x_limit, y_limit), int(x[1]))
           for x in list(zip(range(len(row[1])), row[1]))]) for row in map]

    m3 = [item for sub in m2 for item in sub]
    m4 = {kv[0]: kv[1] for kv in m3}
    return m4
