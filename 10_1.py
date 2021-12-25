a = [[2, 1, 7, 5], [6, 4, 7, 2], [2, 3, 2, 7]]
b = [[6, 3, 2, 1], [1, 6, 3, 2], [2, 5, 7, 2]]


class Matrix:
    def __init__(self, lists):
        self.lists = lists

        def __str__(self):
            return '\n'.join(map(str, self.lists))

        def __add__(self, other):
            x = []
            for i in range(len(self.lists)):
                x.append([])
                for y in range(len(self.lists[0])):
                    x[i].append(self.lists[i][y] + other.lists[i][y])
            return '\n'.join(map(str, x))


matrix_1 = Matrix(a)
matrix_2 = Matrix(b)
print(f"Matrix 1\n{matrix_1}\n{'-' * 20}")
print(f"Matrix 2\n{matrix_2}\n{'-' * 20}")
print(f"matrix 1 + matrix 2\n{matrix_1 + matrix_2}")

