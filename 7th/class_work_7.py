def function1(param):
    """
    es esmu dokumentācija
    """
    print(param)

thing = "stuff"
function1(thing)


def adder(a, b):
    c = a + b
    return c

My_val = adder(5, 10)
print(My_val)
print(adder(adder(5, 20), 50))

def mult(a, b):
    return a*b

big_result = mult(adder(5, 10), mult(2, 20))
print(big_result)

def big_calc(a,b,c):
    result = mult(adder(a,b), adder(b,c))
    return result

print(big_calc(2,3,4))



def lazy_square(a=10, b=2, pretty_print=False):
    result = a**b
    if pretty_print:
        print(f"Cool {a=} raised in {b=} is {result}")
    return result

print(lazy_square())
print(lazy_square(a = 2, b = 4, pretty_print=True))


def super_add(*argv):
    for arg in argv:
        print(arg)


super_add("stuff", "and", 5, "things")


my_list = [1,2,3]
def mod_list(arg_list):
    arg_list.append(10)
    arg_list += [20]
    # arg_list = arg_list + [20] will create a new list
    return(arg_list)

print(my_list)
mod_list(my_list)
print(my_list)
