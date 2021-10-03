D = {'name': 'Satish', 'age': 30, 'gender': "M"}

counter = 1
for i in (dir(D)):
    if not i.ljust(8).startswith('__'):
        print(f"{counter}. {i}()")
        counter += 1

print("D      :  ", D)
print("copy      :  ", D.copy())
print("fromkeys  :  ", D.fromkeys((1, 2, 'Satish', 4, 5), None))
print("get       :  ", D.get('MAMA', 'Not found'))
print("items     :  ", D.items())
print("keys      :  ", D.keys())

D.setdefault('gender', 'male')
print("setdefault:  ", D)

print("update    :  ", D.update({'Country': 'India', 'language': 'Kannada'}))
print("values		:", D.values())

print("popitem   :  ",
      D.popitem())  # remove and return some (key, value) pair as a 2-tuple; but raise KeyError if D is empty.

print("D -- ", D)
print(f"D.pop('age') : {D.pop('age')}")
print("D after popping the age       :  ", D)

print("clear     :  ", D.clear())
