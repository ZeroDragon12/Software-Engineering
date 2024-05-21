def prov(a, c):
    if a is c:
        print(id(a), '==', id(c))
    else:
        print(id(a), '!=', id(c))


def pr(a, c):
    if a != c:
        print(a, '!=', c)
    else:
        print(a, '==', c)


value = [1, 4, 5]
print(id(value))
addition = [3, 83, 2]
print(id(addition))
print()

b = value + addition  # создаёт новый и присваевает уже его
print('+ ', b)
print(id(b))
value += addition  # сразу изменяет список
print('+= ', value)
print(id(value))
print()

prov(value, b)
pr(value, b)
print()

print('сортировка')
print(sorted(value))  # создаёт новый, не изменяя старый
print(value)
list.sort(value)  # сразу сортирует список
print(value)
print()

print('2 вариант')
value = '1'
print(id(value))
addition = '3'
print(id(addition))
print()

b = value + addition
print('+ ', b)
print(id(b))
value += addition
print('+= ', value)
print(id(value))
print()

prov(value, b)
pr(value, b)
