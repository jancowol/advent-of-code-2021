from functools import reduce  # import needed for python3; builtin in python2
from collections import defaultdict

test_input = [
    'start-A',
    'start-b',
    'A-c',
    'A-b',
    'b-d',
    'A-end',
    'b-end',
]

input = [
    'OU-xt',
    'hq-xt',
    'br-HP',
    'WD-xt',
    'end-br',
    'start-OU',
    'hq-br',
    'MH-hq',
    'MH-start',
    'xt-br',
    'end-WD',
    'hq-start',
    'MH-br',
    'qw-OU',
    'hm-WD',
    'br-WD',
    'OU-hq',
    'xt-MH',
    'qw-MH',
    'WD-qw',
    'end-qw',
    'qw-xt']


def test_start():

    cave_map = {
        'start': ['A', 'b'],
        'A': ['start', 'c', 'b', 'end'],
        'b': ['start', 'A', 'd', 'end'],
        'c': ['A'],
        'd': ['b'],
        'end': ['A', 'b']
    }

    result = explore_path(cave_map, 'start', [])
    for r in result:
        print(r)


def test_real_input():
    map = input_to_map(input)
    print('------------------------------------------ start')
    result = explore_path(map, 'start', [])
    for r in result:
        print(r)
    print(len(result))
    end_counts = len(result)
    print(end_counts)
    print('------------------------------------------ end')


def test_map_real_input():
    map = input_to_map(input)

    for m in map.items():
        print(m)


def test_can_identify_small_cave():
    small_cave = 'abc'
    large_cave = 'ABC'

    assert is_small_cave(small_cave) == True
    assert is_small_cave(large_cave) == False


def test_part2():
    test_input = [
        'fs-end',
        'he-DX',
        'fs-he',
        'start-DX',
        'pj-DX',
        'end-zg',
        'zg-sl',
        'zg-pj',
        'pj-he',
        'RW-he',
        'fs-DX',
        'pj-RW',
        'zg-RW',
        'start-pj',
        'he-WI',
        'zg-he',
        'pj-fs',
        'start-RW']
    map = input_to_map(test_input)
    result = exp_path2(map, 'start', [])

    assert len(result) == 3509


def explore_path(cave_map, node, path):
    return walk_node_path(cave_map, node, path, non_visited_small_caves)


def exp_path2(cave_map, node, path):
    return walk_node_path(cave_map, node, path, visitable_nodes2)


def walk_node_path(cave_map, node, path, node_filter):
    new_path = list(path)
    new_path.append(node)

    if(node == 'end'):
        return [new_path]

    visitable_nodes = node_filter(cave_map, node, new_path)

    subpaths = []
    for connected_node in visitable_nodes:
        subpath = walk_node_path(
            cave_map, connected_node, new_path, node_filter)
        subpaths.extend(subpath)

    return subpaths


def non_visited_small_caves(cave_map, node, new_path):
    visited_small_caves = list(filter(is_small_cave, new_path))
    connected_nodes = cave_map[node]
    return [node for node in connected_nodes if node not in visited_small_caves]


def visitable_nodes2(cave_map, node, new_path):
    connected_nodes = filter(lambda x: x != 'start', cave_map[node])

    rules = [
        is_large_cave,
        is_end_node,
        node_not_yet_visited,
        small_cave_visited_more_than_once
    ]

    return filter(lambda node: can_visit_node(node, new_path, rules), connected_nodes)


def is_large_cave(node, path): return not is_small_cave(node)
def is_end_node(node, path): return node == 'end'
def node_not_yet_visited(node, path): return path.count(node) == 0


def small_cave_visited_more_than_once(node, path):
    return not any_small_cave_visited_more_than_once(path)


def can_visit_node(node, current_path, rules):
    return any(rule(node, current_path) for rule in rules)


def any_small_cave_visited_more_than_once(current_path):
    small_caves_in_path = find_small_caves_in(current_path)
    cave_visit_counts = count_by_item(small_caves_in_path)

    return any(x == 2 for x in cave_visit_counts.values())


def find_small_caves_in(seq):
    return filter(lambda x: is_small_cave(x), seq)


def count_by_item(nodes):
    counts = {}
    for item in nodes:
        counts[item] = counts.get(item, 0) + 1
    return counts


def is_small_cave(cave_name):
    return cave_name.lower() == cave_name


def input_to_map(input):
    map = {}
    for item in input:
        node1, node2 = item.split('-')
        existing_n1 = map.get(node1, [])
        existing_n1.append(node2)
        map.update({node1: existing_n1})

        existing_n2 = map.get(node2, [])
        existing_n2.append(node1)
        map.update({node2: existing_n2})

    return map
