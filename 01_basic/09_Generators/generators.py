# Normal function
# def square(n):
# 	result = []
# 	for i in range(n+1):
# 		result.append(i*i)
# 	return result
# print(square(10))

# Using generators
# def square(L):
# 	for i in L:
# 		yield(i*i)

# square_nums = square([1,2,3,4,5])
# print(next(square_nums))
# print(next(square_nums))
# print(next(square_nums))

# ---------------------------------------------------

# result = square(10)
# for i in result:
# 	print(i, end=' ')

# ---------------------------------------------------

# Generators using list comprehension
# result = (i*i for i in range(10))
# print(result)
# for i in result:
# 	print(i, end=' ')
