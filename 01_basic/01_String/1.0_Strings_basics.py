s = " HelloWorld!! Work Hard, I am doing good! "

# Prints all available attributes and methods for strings
print(dir(s))  
# Prints documentation for the `str.lower()` method
print(help(str.lower))  

print("capitalize  : ", s.capitalize())  # Output: " helloworld!! work hard, i am doing good!"
print("casefold    : ", s.casefold())    # Output: " helloworld!! work hard, i am doing good! "
print("center      : ", s.center(50))    # Output: "       HelloWorld!! Work Hard, I am doing good!       "
print("count       : ", s.count("d"))    # Output: 4
print("encode      : ", s.encode())      # Output: b' HelloWorld!! Work Hard, I am doing good! '
print("endswith    : ", s.endswith("od! "))  # Output: True
print("expandtabs  : ", s.expandtabs())  # Output: " HelloWorld!! Work Hard, I am doing good! " (no effect since no tabs are present)
print("find        : ", s.find("W", 10, -1))  # Output: 12
print("format      : ", s.format())      # Output: " HelloWorld!! Work Hard, I am doing good! "

# The `format_map()` and `index()` methods are commented out as they are not used.

print("isalnum     : ", s.isalnum())  # Output: False (due to special characters and spaces)
print("isalpha     : ", s.isalpha())  # Output: False (due to spaces and special characters)
print("isascii     : ", s.isascii())  # Output: True (all characters are ASCII)
print("isdecimal   : ", s.isdecimal())  # Output: False (contains non-numeric characters)

s1 = '12345'
print("isdigit     : ", s1.isdigit())  # Output: True

s3 = 'def'
print("isidentifier: ", s3.isidentifier())  # Output: True (valid Python identifier)
print("islower     : ", s.islower())  # Output: False
print("isnumeric   : ", s.isnumeric())  # Output: False

print("isspace     : ", s.isspace())  # Output: False (contains non-whitespace characters)
print("istitle     : ", s.istitle())  # Output: False (not all words start with capital letters)
print("isupper     : ", s.isupper())  # Output: False

print("join        : ", '.'.join(['ab', 'pq', 'rs']))  # Output: "ab.pq.rs"
print("ljust       : ", s.ljust(200) + "Left Justified")  # Output: s with spaces to make it 200 characters long, followed by "Left Justified"
print("lower       : ", s.lower())  # Output: " helloworld!! work hard, i am doing good! "
print("lstrip      : ", s.lstrip())  # Output: "HelloWorld!! Work Hard, I am doing good! " (leading spaces removed)

print("replace     : ", s.replace("H", "M"))  # Output: " MelloWorld!! Work Mard, I am doing good! "

print("rjust       : ", s.rjust(100))  # Output: s right-aligned with spaces added to make it 100 characters wide
print("rsplit      : ", s.rsplit("W", 10))  # Output: [' Hello', 'orld!! Work Hard, I am doing good! ']
print("rstrip      : ", s.rstrip())  # Output: " HelloWorld!! Work Hard, I am doing good!" (trailing space removed)
print("split       : ", s.split())  # Output: ['HelloWorld!!', 'Work', 'Hard,', 'I', 'am', 'doing', 'good!']

s = "NIteen \n Satish"
print("splitlines  : ", s.splitlines())  # Output: ['NIteen ', ' Satish']
print("startswith  : ", s.startswith("World", 3, 10))  # Output: False
print("strip       : ", s.strip())  # Output: "NIteen \n Satish" (no leading or trailing spaces)
print("swapcase    : ", s.swapcase())  # Output: "niTEEN \n sATISH"
print("title       : ", s.title())  # Output: "Niteen \n Satish"
print("upper       : ", s.upper())  # Output: "NITEEN \n SATISH"
