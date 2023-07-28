sentense = 'This is a sentence'
print(sentense[17])
print(sentense[-1])
print(sentense[-3])
print(sentense[-0])
print(sentense[0:4])
print(sentense[5:7])

sentense = 'abcdefg'

print(sentense[0:7:1])
print(sentense[0:7:2])
print(sentense[3:])

sentense = 'This is a sentence'
print(sentense.upper())
print(sentense.capitalize())

sentense = 'abc avc'
print(sentense.isdigit())

sentense = '12312312312'
print(sentense.isdigit())

sentense = 'A12%312'
print(sentense.startswith('A'))
print(sentense.startswith('%',3))