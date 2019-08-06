seen = {}


def towers_of_hanoi_moves(n):
    if n == 1:
        return [(1, 3)]
    elif n == 2:
        return [(1, 2), (1, 3), (2, 3)]
    else:
        if n not in seen:
            seen[n] = pivot(towers_of_hanoi_moves(n - 1), 2, 3) + \
                towers_of_hanoi_moves(
                1) + pivot(towers_of_hanoi_moves(n - 1), 1, 2)
        return seen[n]


def slow_towers_of_hanoi_moves(n, seen={}):
    if n == 1:
        return [(1, 3)]
    elif n == 2:
        return [(1, 2), (1, 3), (2, 3)]
    else:
        return pivot(towers_of_hanoi_moves(n - 1), 2, 3) + \
            towers_of_hanoi_moves(
            1) + pivot(towers_of_hanoi_moves(n - 1), 1, 2)


def pivot(lst_of_tuples, switch1, switch2):
    return [swap(tup, switch1, switch2) for tup in lst_of_tuples]


def swap(tup, switch1, switch2):
    index0 = None
    index1 = None
    if tup[0] == switch1:
        index0 = switch2
    elif tup[0] == switch2:
        index0 = switch1
    else:
        index0 = tup[0]
    if tup[1] == switch1:
        index1 = switch2
    elif tup[1] == switch2:
        index1 = switch1
    else:
        index1 = tup[1]
    return (index0, index1)


if __name__ == '__main__':
    for i in range(1):
        # slow_towers_of_hanoi_moves(2)
        towers_of_hanoi_moves(24)
