# from typing import int
# Type 1
def add(var1, var2):
    # type: (int, int) -> float
    return float(var1 + var2)


# Type 2
def string_add(var1: str, var2: str) -> str:
    return var1 + var2


print(add(10, 20))
print(string_add('Satish', 'Chougule'))
