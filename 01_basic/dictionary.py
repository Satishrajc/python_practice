D = {'name': 'Satish', 'age': 30, 'gender': "M"}

# for i in dir(D):
# 	print(i)


print("copy      :  ", D.copy())
print("fromkeys  :  ", D.fromkeys(((1,2),(3,4))))
print("get       :  ", D.get('name', 'Not found'))
print("items     :  ", D.items())
print("keys      :  ", D.keys())

D.setdefault('gender', 'male')
print("setdefault:  ", D)

print("update    :  ", D.update({'Country': 'India'}))
print("values		:", D.values())

print("popitem   :  ", D.popitem())  # remove and return some (key, value) pair as a 2-tuple; but raise KeyError if D is empty.

D.pop('age')
print("pop       :  ", D)

print("clear     :  ", D.clear())
