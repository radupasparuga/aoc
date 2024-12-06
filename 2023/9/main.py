with open("input.txt", "r") as f:
    input_data = f.readlines()


def extrapolate(xs):
    if not any(xs):
        return 0

    return xs[-1] + extrapolate([b - a for a, b in zip(xs, xs[1:])])


def predict_next(array):
    if not any(element != 0 for element in array):
        return 0
    diff = []
    # print(array)
    for i in range(0, len(array) - 1):
        diff.append(abs(array[i] - array[i + 1]))
        # print(array[i], array[i + 1])
    result = predict_next(diff)
    # print(array, array[-1] + result)
    return array[-1] + result


def aoc09():
    def compute(L):
        total = 0
        while any(L):
            total += L[-1]
            L = [L[i + 1] - L[i] for i in range(len(L) - 1)]
        return total

    d = [list(map(int, ligne.split())) for ligne in open("input.txt")]
    print(sum(compute(L) for L in d))  # part 1
    print(sum(compute(L[::-1]) for L in d))  # part 2


sum1 = 0
sum2 = 0
for line in input_data:
    array = [int(x) for x in line.split()]
    # print(extrapolate(array))
    sum1 += extrapolate(array)
    sum2 += predict_next(array)
print(sum1, sum2)

aoc09()
