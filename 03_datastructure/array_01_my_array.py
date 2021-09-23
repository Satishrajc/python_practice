import ctypes


class Array:
    def __init__(self):
        self.length = 0
        self.capacity = 1
        # self.aArray = self._make_size(self.capacity)
        self.dummyArray = [None]

    def append(self, element):
        self.dummyArray[self.length] = element
        self.length += 1

    def __len__(self):
        return len(self.dummyArray)

    def __getitem__(self, item):
        return self.dummyArray[item]

    def __str__(self):
        return f'{self.dummyArray}'

    def _resize(self):
        B = (2 * self.capacity * ctypes.py_object)()

        for i in range(self.length):
            B[i] = self.dummyArray[i]

        self.A = B





zArray = Array()

zArray.append(10)

print(zArray)
print(len(zArray))

zArray.append(20)
print(zArray)