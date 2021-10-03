s = " HelloWorld!! Work Hard, I am doing good! "
print(dir(s))
print(help(str.lower))
print("capitalize  : ", s.capitalize())
print("casefold    : ", s.casefold())
print("center      : ", s.center(50))
print("count       : ", s.count("d"))
print("encode      : ", s.encode())
print("endswith    : ", s.endswith("od! "))
print("expandtabs  : ", s.expandtabs())
print("find        : ", s.find("W", 10, -1))
print("format      : ", s.format())
# print("format_map  : ", s.format_map())
# print("indindex    : ", s.indindex())
print("isalnum     : ", s.isalnum())  # Return True if the string is an alpha-numeric string, False otherwise.
print("isalpha     : ", s.isalpha())  # Return True if the string is an alphabetic string, False otherwise.
print("isascii     : ", s.isascii())  # Return True if all characters in the string are ASCII, False otherwise.
print("isdecimal   : ", s.isdecimal())  # Return True if the string is a decimal string, False otherwise.
s1 = '12345'
print("isdigit     : ", s1.isdigit())  # Return True if the string is a digit string, False otherwise.
s3 = 'def'
print("isidentifier: ",
      s3.isidentifier())  # Return True if the string is a valid Python identifier(keywords), False otherwise.
print("islower     : ", s.islower())
print("isnumeric   : ", s.isnumeric())
# print("isprintable : ", s.isprintable())
print("isspace     : ", s.isspace())  # Return True if the string is a whitespace string, False otherwise.
print("istitle     : ", s.istitle())  # Return True if the string is a title-cased string, False otherwise.
print("isupper     : ", s.isupper())
print("join        : ", '.'.join(['ab', 'pq', 'rs']))  # Ans -> 'ab.pq.rs' ) --> The result is returned as a new string
print("ljust       : ", s.ljust(200) + "Left Justified")
print("lower       : ", s.lower())
print("lstrip      : ", s.lstrip())
# print("maketrans   : ", s.maketrans())
# print("partition   : ", s.partition())
print("replace     : ", s.replace("H", "M"))
# print("rfind       : ", s.rfind())
# print("rindex      : ", s.rindex())
print("rjust       : ", s.rjust(100))
# print("rpartition  : ", s.rpartition())
print("rsplit      : ",
      s.rsplit("W", 10))  # Splits are done starting at the end of the string and working to the front.
print("rstrip      : ", s.rstrip())  # Return a copy of the string with trailing whitespace removed.
print("split       : ", s.split())

s = "NIteen \n Satish"
print("splitlines  : ", s.splitlines())  # Return a list of the lines in the string, breaking at line boundaries.
print("startswith  : ", s.startswith("World", 3, 10))
print("strip       : ", s.strip())  # Return a copy of the string with leading and trailing whitespace remove.
print("swapcase    : ",
      s.swapcase())  # Convert uppercase characters to lowercase and lowercase characters to uppercase.
print("title       : ", s.title())
# print("translate   : ", s.translate())
print("upper       : ", s.upper())
# print("zfill       : ", s.zfill(10))
