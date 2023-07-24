def add (a,b):
    print(f"adding: {a} + {b}")
    return a + b

def div(a,b):
    try:
        print(f"dividing: {a} + {b}")
        return a/b
    except ZeroDivisionError as err:
        print(err)
    
    return None

def test_add_numbers():
    result = add(2, 3)
    assert result == 5

def test_neg_add():
    result = add(2, 3)
    assert result == 6
