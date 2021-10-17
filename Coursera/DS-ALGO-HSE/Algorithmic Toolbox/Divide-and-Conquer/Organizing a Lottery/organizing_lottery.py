# python3
from sys import stdin
from bisect import bisect_left, bisect_right


def points_cover_naive(starts, ends, points):
    assert len(starts) == len(ends)
    count = [0] * len(points)

    for index, point in enumerate(points):
        for start, end in zip(starts, ends):
            if start <= point <= end:
                count[index] += 1

    return count


def points_cover(starts, ends, points):
    result = [0] * len(points)
    counter = 0
    starts = [(starts[i], 0, 0) for i in range(len(starts))]
    ends = [(ends[i], 2, 0) for i in range(len(ends))]
    points = [(points[i], 1, i) for i in range(len(points))]
    all_points = sorted(starts + ends + points, key=lambda x: (x[0], x[1]))
    for i in range(len(all_points)):
        if all_points[i][1] == 0:
            counter += 1
        if all_points[i][1] == 2:
            counter -= 1
        if all_points[i][1] == 1:
            result[all_points[i][2]] += counter

    return result


if __name__ == '__main__':
    data = list(map(int, stdin.read().split()))
    n, m = data[0], data[1]
    input_starts, input_ends = data[2:2 * n + 2:2], data[3:2 * n + 2:2]
    input_points = data[2 * n + 2:]

    output_count = points_cover(input_starts, input_ends, input_points)
    print(*output_count)
