

def div(a,b):
    try:
        print(f"Divide: {a}/{b}")
        result = a/b
        # raise FileNotFoundError("custom message")
    
    except ZeroDivisionError:
        print("ZeroDivisionError")
        result = None
        
    except Exception as err:
        print(f"Other Error: {err}")
        
    else:
        print("Error does not occur")
        
    finally:
        print("Execute every time")
        return result
    
    
# print(div(10, 5))
print(div(2, 0))