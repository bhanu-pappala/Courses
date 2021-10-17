# python3

from collections import namedtuple
from sys import stdin

Segment = namedtuple('Segment', 'start end')


def compute_optimal_points(segments):
    points = []

    segments.sort(key=lambda x: x[1])
    max_right = segments[0][1]
    points.append(max_right)
    i = 1
    while i < len(segments):
        if max_right < segments[i][0]:
            max_right = segments[i][1]
            points.append(max_right)
        i += 1

    return points

print(compute_optimal_points([Segment(4, 7), Segment(1, 3), Segment(2, 5), Segment(5, 6)]))

# if __name__ == '__main__':
#     n, *data = map(int, stdin.read().split())
#     input_segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
#     assert n == len(input_segments)
#     output_points = compute_optimal_points(input_segments)
#     print(len(output_points))
#     print(*output_points)
