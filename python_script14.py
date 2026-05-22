# ------ 1:

strings = ["apple23", "ban1ana45", "12cherry", "grape3", "blue23berry"]

result = []

for str in strings:
    digit_started = False
    is_valid = True

    for chr in str:
        if chr.isdigit():
            digit_started = True

        elif chr.isalpha() and digit_started:
            is_valid = False
            break

    if is_valid and digit_started:
        result.append(str)
      
print(result)



# ------ 2:

numbers = [1, 3, 6, 9, 10, 12, 15, 19, 20]

num_b = int(input("Введите число для удаления кратных ему элементов:" ))

result = [num for num in numbers if num % num_b != 0]

print(f"Список без кратных значений: {result}")


# ------ 3:


numbers = [5, 2, 3, 8, 4, 1, 2, 7]

even_numbers = iter(sorted([num for num in numbers if num % 2 == 0], reverse=True))

result = []

for num in numbers:
    if num % 2 == 0:
        result.append(next(even_numbers))
    else:
        result.append(num)

print(result)

