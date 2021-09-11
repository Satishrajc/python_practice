# 01 - Create a function with variable length of arguments
def foo(arg1, *arg2, **arg3):
    print(arg1, arg2, arg3)


# Kind of method overriding but need to check
foo(10, 1, 2, 3, 4, 5, a=1, b=3, c=3)
foo(10, 1, a=1)


# --------------------------------------------------- #
# 02- Return multiple values from a function
def foo(arg1):
    return 1, 2, 3, 4


print(foo("param1"))


# --------------------------------------------------- #
# 03- Create a function with default argument
def foo(arg1, arg2=20, arg3=4, arg4=None):
    print(arg1, arg2, arg3, arg4)


# wrong --> foo(arg4="Something", "param1" )
# positional argument should come after keyword argument


foo("Hello", arg4="Something")


# --------------------------------------------------- #
# 04 - Assign a different name to function and call it through the new name
def display_student(name, age):
    print(name, age)


# call using original name
display_student("Emma", 26)

# assign new name
showStudent = display_student
# call using new name
showStudent("Emma", 26)


# --------------------------------------------------- #
# 05 - Generate a Python list of all the even numbers between 4 to 30
def give_even_numbers(start, stop):
    # even_numbers = []
    # for i in range(start, stop):
    #     if i%2 == 0:
    #         even_numbers.append(i)

    even_numbers = [i for i in range(start, stop) if i % 2 == 0]
    return even_numbers


print(give_even_numbers(10, 20))


# --------------------------------------------------- #
# 6 - Find the largest item from a given list
def find_larger(arg):
    large = 0
    for item in arg:
        if item > large:
            large = item
    return large


L = [1, 2, 3, 42, 10, 0]
print(find_larger(L))

# --------------------------------------------------- #
# --------------------------------------------------- #
# --------------------------------------------------- #
# --------------------------------------------------- #
# --------------------------------------------------- #
# --------------------------------------------------- #
# --------------------------------------------------- #
# --------------------------------------------------- #
# --------------------------------------------------- #
# --------------------------------------------------- #
# --------------------------------------------------- #
# --------------------------------------------------- #
# --------------------------------------------------- #
