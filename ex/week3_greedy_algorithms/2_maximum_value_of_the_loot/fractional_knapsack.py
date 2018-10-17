# Uses python3
import sys

# 3 50 60 20 100 50 120 30


def get_optimal_value(capacity, weights, values):

    assert len(weights) == len(values)

    value = 0.
    cur_cap = 0.

    uni_val = [v/w for v, w in zip(values, weights)]
    # uni_val.sort()
    idx = sorted(range(len(uni_val)), reverse=True, key=lambda k: uni_val[k])

    # s_uni_val = uni_val[idx]
    # s_weights = weights[idx]
    # s_values = values[idx]

    for i in idx:
        if cur_cap < capacity:
            # break
            cur_wei = min(weights[i], capacity-cur_cap)
            value = value + uni_val[i] * cur_wei
            cur_cap = cur_cap + cur_wei

    return value


if __name__ == "__main__":
    data = list(map(int, sys.stdin.read().split()))
    n, capacity = data[0:2]
    values = data[2:(2 * n + 2):2]
    weights = data[3:(2 * n + 2):2]
    opt_value = get_optimal_value(capacity, weights, values)
    print("{:.10f}".format(opt_value))
