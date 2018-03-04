DATA_FILE = "graph_input.txt"
DATA_OUT = "Вершины: {}"
OUT = '''Самое 'тяжелое' независимое множество: {vertices}
Вес: {weight}'''

VERTICES_KEY = "vertices"
WEIGHT_KEY = "weight"


def main():
    w_arr = data_input(DATA_FILE)
    print(DATA_OUT.format(w_arr))
    res = process(w_arr)
    print(OUT.format(vertices=res.get(VERTICES_KEY), weight=res.get(WEIGHT_KEY)))


def data_input(filename: str):
    with open(filename) as f:
        w_arr = [float(num) for num in f.readline().rsplit(' ')]
    return w_arr


def new_entry(vertices: list, weight: float):
    return {
        VERTICES_KEY: vertices,
        WEIGHT_KEY: weight
    }


def process(w_arr):
    T = [new_entry([0], w_arr[0])]

    if len(w_arr) > 1:
        if w_arr[1] < w_arr[0]:
            T.append(T[0])
        else:
            T.append(new_entry([1], w_arr[1]))

    if len(w_arr) > 2:
        for i in range(2, len(w_arr)):
            w_sum = w_arr[i] + T[i - 2].get(WEIGHT_KEY)

            if w_sum < T[i - 1].get(WEIGHT_KEY):
                T.append(T[i - 1])
            else:
                vertices = T[i - 2].get(VERTICES_KEY).copy()
                vertices.append(i)
                T.append(new_entry(vertices, w_sum))

    dout = "T[{}]: {} -> {}"
    for i in range(0, len(T)):
        print(dout.format(i, T[i].get(WEIGHT_KEY), T[i].get(VERTICES_KEY)))

    return T[-1]


main()

# 1 8 6 3 6

# example for a) and b)
# 8 4 1 3 10 9
# a: 10 + 8 + 1 = 19
# b: 10 + 8 + 1 = 19
# actual: 8 + 3 + 9 = 20

