
'''
order a list of numbers without built-in sort, min, max function
'''
data_list = [-5, -23, 5, 0, 23, -6, 23, 67]
sorted_list = []

while data_list:
    minimum = data_list[0]  # arbitrary number in list 
    for x in data_list: 
        if x < minimum:
            minimum = x
    sorted_list.append(minimum)
    data_list.remove(minimum)    

print(sorted_list)