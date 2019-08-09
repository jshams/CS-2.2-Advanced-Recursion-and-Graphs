seen = {}


def towers_of_hanoi_moves(n):
    if n == 1:
        return [(1, 3)]
    else:
        if n not in seen:
            toh_n_minus_one = towers_of_hanoi_moves(n - 1)
            pivoted = pivot_twice(toh_n_minus_one)
            seen[n] = pivoted[0] + [(1, 3)] + pivoted[1]
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


def pivot_twice(lst_of_tuples):
    return [swap(tup, 2, 3) for tup in lst_of_tuples], [swap(tup, 1, 2) for tup in lst_of_tuples]


def swap(tup, switch1, switch2):
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
    import sys
    n = 3
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    z = towers_of_hanoi_moves(n)
    print(
        f'With {n} rings in our tower the minumum number of moves is: {len(z)}')
    print('And the moves are:')
    # [print(f'{i + 1}. {y}') for i, y in enumerate(z)]
    print(z)
