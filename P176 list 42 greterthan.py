numbers = [11, 44, 500, 22, 99, 77, 200, 66, 2, 11, 22]
value = int(input("Enter greater than value: "))
greater_numbers = []
for num in numbers:
    if num > value:
        greater_numbers.append(num)
print("Numbers greater than", value, ":", *greater_numbers)


