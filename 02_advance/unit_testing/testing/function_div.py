def div(a,b):
    try:
        print(f"dividing: {a} + {b}")
        return a/b
    except ZeroDivisionError as err:
        print(err)
    
    return None

    