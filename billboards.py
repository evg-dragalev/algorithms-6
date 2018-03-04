DATA_FILE = "bb_input.txt"
DISTANCE = 5
DATA_OUT = '''M = {M}
n = {n}
X = {X}
R = {R}
'''
RES_OUT = '''Индексы: {ind}
Максимальная прибыль: {profit}'''

PROFIT_KEY = "profit"
INDEXES_KEY = "indexes"


def main():
    data = data_input(DATA_FILE)
    print(DATA_OUT.format(
        M=data.get("M"),
        n=data.get("n"),
        X=data.get("X"),
        R=data.get("R")
    ))
    res = process(
        data.get("n"),
        data.get("M"),
        data.get("X"),
        data.get("R")
    )
    print(RES_OUT.format(
        ind=res.get(INDEXES_KEY),
        profit=res.get(PROFIT_KEY)
    ))


def data_input(filename: str):
    with open(filename) as f:
        m = float(f.readline())
        n = int(f.readline())
        x_arr = [float(num) for num in f.readline().rsplit(' ')]
        r_arr = [float(num) for num in f.readline().rsplit(' ')]
    return {
        "n": n,
        "M": m,
        "X": x_arr,
        "R": r_arr
    }


def new_entry(indexes: list, profit: float):
    return {
        INDEXES_KEY: indexes,
        PROFIT_KEY: profit
    }


def process(n: int, m: float, x: list, r: list):
    T = [new_entry([], 0)]
    x.insert(0, 0)
    r.insert(0, 0)

    for i in range(1, n+1):
        k = i-1
        while x[i] - x[k] <= DISTANCE and k > 0:
            k -= 1

        profit = T[k].get(PROFIT_KEY) + r[i]
        if profit < T[i-1].get(PROFIT_KEY):
            T.append(T[i-1])
        else:
            indexes = T[k].get(INDEXES_KEY).copy()
            indexes.append(i)
            T.append(new_entry(indexes, profit))

    dout = "T[{}]: {} -> {}"
    for i in range(0, len(T)):
        print(dout.format(i, T[i].get(PROFIT_KEY), T[i].get(INDEXES_KEY)))

    return T[-1]


main()


# 30
# 15
# 1 3 5 7 9 10 15 16 17 19 22 23 26 27 28
# 23 32 32 40 50 29 6 50 47 14 36 16 43 35 5

# 20
# 4
# 6 7 12 14
# 5 6 5 1
