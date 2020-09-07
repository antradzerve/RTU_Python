numbers = input("Enter three numbers with space between them: ")

number_list = numbers.split(" ")
max_number = number_list.pop(number_list.index(max(number_list)))

def add_mult(a, b, c):
    result = (a+b)*c
    return result

print(add_mult(int(number_list[0]), int(number_list[1]), int(max_number)))