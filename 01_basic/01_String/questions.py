# ------------------------------------------------ #
# 1. Take a srting and check for alnum, alpha, digit, uppercase and print true
# take input randomly
s = input("Input string :")
# import re
#
# # alnum, alph, digit, uppercase
#
# if s.isalnum():
#     print('isalnum : ', True)
# else:
#     print('isalnum : ', False)
#
# if re.search('[a-z]', s) or re.search('[A-Z]', s):
#     print("alph: ", True)
# else:
#     print('alph : ', False)
#
# if re.search('[0-9]', s):
#     print("digit : ", True)
# else:
#     print('digit : ', False)
#
# if re.search('[A-Z]', s):
#     print("uppercase: ", True)
# else:
#     print('uppercase : ', False)

# resDict = {'alnum': False, 'alpha': False, 'digit':False, 'uppercase': False}
resDict = {}
resDict.fromkeys(('alnum', 'alpha', 'digit', 'uppercase'), False)
for i in s:
    if i.isalpha():
        resDict['alpha'] = True
    if i.isdigit():
        resDict['digit'] = True
    if i.isupper():
        resDict['uppercase'] = True

resDict['alnum'] = resDict['alpha'] and resDict['digit']

print(resDict.values())

# ------------------------------------------------ #
