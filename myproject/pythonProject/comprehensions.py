# list comprehensions
hello_list = [char for char in "hello"]
print(hello_list)

num_list = [num for num in range(0, 100)]
print(num_list)

mult_list = [num*2 for num in range(0, 100)]
print(mult_list)

even_list = [num**2 for num in range(0, 100) if num % 2 == 0]
print(even_list)

# dictionary comprehensions
simple_dict = {
    "a": 1,
    "b": 2
}
my_dict = {key: value**2 for key, value in simple_dict.items() if value % 2 != 0}
print(my_dict)
my_dict2 = {num: num*2 for num in [1, 2, 3]}
print(my_dict2)
