# Дан кортеж, задача определить площадь какой пары будет максимальной. S = a*b, где a и b - длины полуосей эллипса.
# find_farthest_orbit(list_of_orbits)

from random import randint


def general_sequence_of_orbits(count_of_orbits: int) -> tuple[int, int]:
    result = [(randint(1, 10), randint(1, 10)) for _ in range(count_of_orbits)]
    return result


def find_farthest_orbit(list_of_orbits: list[tuple[int, int]]) -> tuple[int, int]:
    squares = [(i, e[0] * e[1]) for i, e in enumerate(list_of_orbits) if e[0] != e[1]]
    # squares = tuple()
    # for i, e in enumerate(list_of_orbits):
    #     if e[0] != e[1]:
    #         squares[e] = e[0] * e[1]
    max_square = max(squares, key=lambda x: x[1])
    return list_of_orbits[max_square[0]]


orbits = general_sequence_of_orbits(10)
print(orbits)
print(find_farthest_orbit(orbits))
