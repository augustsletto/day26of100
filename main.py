numbers = [1, 2, 3]

new_list = [n + 1 for n in numbers]

print(new_list)




name = "August"

new_list = [letter for letter in name]

print(new_list)



rng_list = [num * 2 for num in range(1, 5) if 5 == 5]

print(rng_list)



names = ["August hej", "Emma hej", "Sixten", "Chrille"]


short_names = [name for name in names if len(name) < 12]
print(short_names)

long_names = [name.capitalize() for name in names if len(name) < 18]
print(long_names)


list_of_strings = ['9', '0', '32', '8', '2', '8', '64', '29', '42', '99']
numbers = [int(num) for num in list_of_strings]
result = [num for num in numbers if num % 2 == 0]
print(result)