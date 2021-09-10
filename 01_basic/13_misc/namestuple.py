from collections import namedtuple

Color = namedtuple('Color', ['red', 'green', 'blue'])

color = Color(100, 150, 200)

print(color[0])
print(color.blue)

# --------------------------------
color = Color(red=12, green=255, blue=255)
print(color[0])
print(color.blue)
