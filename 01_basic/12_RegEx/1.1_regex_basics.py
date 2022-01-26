import re

string = "I am happy! Sati.cou@gmail.com 11-11-2015 rakesh_chou@shinal.yahoo"

pattern = re.compile(r"[a-zA-Z_.]+@[a-zA-Z]+.[a-zA-Z]+")

match = re.finditer(pattern, string)

for i in match:
    print(i)
