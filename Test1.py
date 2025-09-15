print("Dictionaries examples")

dict1={'name':'david','age':10,'class':5}
print(dict1)

print(dict1['age'])
print(dict1['class'])

print(dict1.get('name','Not found'))

print(dict1.pop(10,'Not Found'))
dict1.clear()
print(dict1)
