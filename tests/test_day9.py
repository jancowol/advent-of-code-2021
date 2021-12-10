from dataclasses import dataclass
from advent.file_utils import read_file
from functools import reduce
from collections import namedtuple

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
    m4 = build_map_from(test_input)
    print('******************* map building')
    print(m4)


def test_can_find_low_points():
    map = build_map_from(test_input)
    result = sum_low_point_risks(map)
    assert result == 15


def test_actual_data():
    input = read_file('day9-input')
    map = build_map_from(input)
    result = sum_low_point_risks(map)
    print(result)


# def test_basins():
#     input = read_file('day9-input')
#     x_limit = len(input[0]) - 1
#     y_limit = len(input) - 1
#     map = build_map_from(input)
#     low_points = find_low_points(map)

#     basins = [compute_basin(x, set([x]), x_limit, y_limit, map)
#               for x in low_points]
#     basin_sizes = sorted([len(basin) for basin in basins], reverse=True)[:3]
#     print(basin_sizes)
#     foo = reduce(lambda x, y: x * y, basin_sizes)
#     print('**************** part 2 final answer')
#     print(foo)


def test_named_tuple():
    foo = IndexedItem(0, 0)
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


IndexedItem = namedtuple('IndexedItem', ['index', 'item'])


def build_map_from(input):
    map_width = len(input[0])
    map_height = len(input)

    lines_with_y = zip(range(map_height), input)

    m2 = [([(Point(x[0], row[0], map_width - 1, map_height - 1), int(x[1]))
           for x in zip(range(len(row[1])), row[1])]) for row in lines_with_y]

    m3 = [item for sub in m2 for item in sub]
    m4 = {kv[0]: kv[1] for kv in m3}
    return m4


def test_map_build3():
    map_width = len(test_input[0])
    map_height = len(test_input)

# def test_map_build2():
#     m4 = build_map_from2(test_input)
#     foo = list(m4)
#     print('~~~~~~~~~~~~~~~~~~~')
#     for f in foo:
#         # print(f)
#         print(f[0])
#         for b in f[1]:
#             print('...')
#             print(b)
#     print(range(300))
#     # print(foo)


# def build_map_from2(input):
#     map_width = len(input[0])
#     map_height = len(input)

#     lines_with_y = zip(range(map_height), input)
#     # xxx = zip(range(map_width), x[1])
#     lwy = ((x[0], map(lambda item: (item[0], int(item[1])), zip(range(map_width), x[1])))
#            for x in lines_with_y)

#     boo = list(lwy)
#     # print('222222222222222222222 map building')
#     # for item in boo:
#     #     print(f'{item[0]}: {list(item[1])}')
#     # lwy = (IndexedItem(index=x[0], item=[IndexedItem(0, reading)
#     #        for reading in x[1]]) for x in zip(range(map_height), input))
#     return boo
