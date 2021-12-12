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

    # cave_map = input_to_map(test_input)

    print('******************')
    result = explore_path(cave_map, 'start', 0, [])
    for r in result:
        print(r)


def test_real_input():
    map = input_to_map(input)
    print('------------------------------------------ start')
    result = explore_path(map, 'start', 0, [])
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


def test_identify_small_cave():
    small_cave = 'abc'
    large_cave = 'ABC'

    assert is_small_cave(small_cave) == True
    assert is_small_cave(large_cave) == False


def explore_path(cave_map, node, fork_count, path):
    new_path = list(path)
    new_path.append(node)

    if(node == 'end'):
        return [new_path]

    exclude_nodes = [x for x in new_path if is_small_cave(x)]
    connected_nodes = cave_map[node]
    connected_nodes_to_visit = [
        x for x in connected_nodes if x not in exclude_nodes]

    subpaths = []
    for connected_node in connected_nodes_to_visit:
        subpath = explore_path(cave_map, connected_node,
                               fork_count + 1, new_path)
        subpaths.extend(subpath)

    return subpaths


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
    result = explore_path2(map, 'start', 0, [])

    assert len(result) == 3509


def explore_path2(cave_map, node, fork_count, path):
    new_path = list(path)
    new_path.append(node)

    if(node == 'end'):
        return [new_path]

    connected_nodes = [x for x in cave_map[node] if x != 'start']
    connected_nodes_to_visit = [
        x for x in connected_nodes if can_visit_node(x, new_path)]

    subpaths = []
    for connected_node in connected_nodes_to_visit:
        subpath = explore_path2(cave_map, connected_node,
                                fork_count + 1, new_path)
        subpaths.extend(subpath)

    return subpaths


def can_visit_node(node, current_path):
    current_cave_is_small = is_small_cave(node)
    if(not current_cave_is_small):
        return True

    if(node == 'start'):
        return False

    if(node == 'end'):
        return True

    small_caves_in_current_path = [x for x in current_path if is_small_cave(x)]

    small_cave_visit_counts = {}
    for item in small_caves_in_current_path:
        small_cave_visit_counts[item] = small_cave_visit_counts.get(
            item, 0) + 1

    node_visit_count = small_cave_visit_counts.get(node, 0)
    if(node_visit_count == 0):
        return True

    has_a_cave_visited_twice = (
        len([x for x in small_cave_visit_counts.values() if x > 1]) > 0)
    return (node_visit_count == 1 and (not has_a_cave_visited_twice))


def groupBy(key, seq):
    return reduce(lambda grp, val: grp[key(val)].append(val) or grp, seq, defaultdict(list))


def is_small_cave(cave_name):
    return cave_name.lower() == cave_name
