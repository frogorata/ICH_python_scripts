numbers = (3, 7, 2, 8, 5, 10, 1)

result = []
max_so_far = float('-inf')

for num in numbers:
    if num > max_so_far:
        result.append(num)
        max_so_far = num

result_tuple = tuple(result)
print(result_tuple)


#------------

numbers = (1, 2, 3, 4, 2, 5, 3, 6, 4, 2, 9)

indexes = {}

for index, key in enumerate(numbers):
    indexes.setdefault(key, []).append(index)

for key, i in indexes.items():
       if len(i) > 1:
        print(f' Индексы элемента {key}:', i)