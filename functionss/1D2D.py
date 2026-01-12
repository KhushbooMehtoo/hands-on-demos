arr = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]


def converter(arr):

    _op = []

    for i in arr:
        for j in i:
            _op.append(j)

    return _op;

x = converter(arr)

print(x)