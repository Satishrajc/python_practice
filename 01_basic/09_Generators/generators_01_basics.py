print("Normal function without generators")


def square(n):
    result = []
    for i in range(n + 1):
        result.append(i * i)
    return result


print(square(10))

print("Function with generators")


def square(aList):
    for i in aList:
        yield i * i


square_nums = square([1, 2, 3, 4, 5])

# Note: Observe tht square is not called directly
print(next(square_nums))
print(next(square_nums))
print(next(square_nums))
print(next(square_nums))
print(next(square_nums))
print(next(square_nums))
