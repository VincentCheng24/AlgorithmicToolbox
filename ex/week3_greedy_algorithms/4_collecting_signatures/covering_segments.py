# Uses python3
import sys
from collections import namedtuple
import numpy as np

Segment = namedtuple('Segment', 'start end')


def optimal_points(segments):
    n = len(segments)
    points = []
    starts = []
    ends = []
    # write your code here
    for s in segments:
        starts.append(s.start)
        ends.append(s.end)

    starts = np.array(starts)
    ends = np.array(ends)

    idx = sorted(range(len(starts)), key=lambda k: starts[k])
    starts = starts[idx]
    ends = ends[idx]

    i = 0

    while i < n:
        idx_buf_a = []
        idx_buf_b = []
        cur_a = starts[i]

        while starts[i] == cur_a and i < n:
            idx_buf_a.append(i)
            i += 1
            if i == n:
                break


        cur_bs = ends[idx_buf_a]
        cur_b = min(cur_bs)

        if i < n:
            while ends[i] <= cur_b and i < n:
                idx_buf_b.append(i)
                i += 1
                if i == n:
                    break

        if len(idx_buf_b) > 0:
            cur_b = min(ends[idx_buf_b])

        points.append(cur_b)

        if i < n:
            while starts[i] <= cur_b and i < n:
                i += 1
                if i == n:
                    break
                # if i == n:
                #     return points

        # if i == n:
        #     break

    return points


def optimal_points_v2(segments):
    points = []
    segments = sorted(segments, key=lambda segment: segment.end)
    current = segments[0].end
    points.append(current)

    for s in segments:
        if current < s.start or current > s.end:
            current = s.end
            points.append(current)

    return points


if __name__ == '__main__':
    input = sys.stdin.read()
    n, *data = map(int, input.split())
    segments = list(map(lambda x: Segment(x[0], x[1]), zip(data[::2], data[1::2])))
    points = optimal_points_v2(segments)
    print(len(points))
    for p in points:
        print(p, end=' ')
