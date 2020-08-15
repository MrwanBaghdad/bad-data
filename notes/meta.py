
print("hello world")

funs = (
        lambda x: x,
        lambda x: x + 1,
        lambda x: x + 2
)


funcs_coerce = {
        'int': lambda x: x,
        'string': lambda x : int(x),
        'float': lambda x: x
    }


StringField = lambda x : str(x)

PrimaryField = lambda values: lambda x: x not in values

compose = lambda f: lambda a : lambda b : f(a(b))

StringFieldCoerce = lambda x: str(x)
FloatFieldCoerce = lambda x: float(x)
GetFirstPart = lambda sep: lambda x: x.split(sep)[0]
pipe = compose(FloatFieldCoerce)(GetFirstPart('-'))



# is 5 unique

arr = [1,1,3,5]
is_equal = lambda a: lambda arr : [i == a for i in arr]
count = lambda a: lambda arr: sum(is_equal(a)(arr))
is_unique = lambda a: lambda arr: count(a)(arr) < 1
all_values_unique = lambda arr: all([is_unique(i)(arr) for i in arr])
assert all_values_unique(arr) is False
assert count(1)(arr) == 2



is_odd = compose(operator.not_)(is_even)
is_odd(3)


mapping = lambda x: match(x,
        1,1,
        is_even, 'even',
        lambda x: x % 3 == 0, 'thrices',
        _, 'odd',
    )





fizzbuzz = lambda x: match(x,
        is_div(15), 'fizzbuzz',
        is_div(3), 'fizz',
        is_div(5), 'buzz',
        _, x,
        )


hexit = lambda x: match(x,
        int, lambda y: hex(y),
        str, x,
        )
hexit(1)

hexfizzbuzz = compose(hexit)(fizzbuzz)
upper_hex_fizzbuzz = compose(lambda x: x.upper())(hexfizzbuzz)
list(map(upper_hex_fizzbuzz, range(100)))

gen_fizz_buzz = lambda fizbuzfunc: lambda n : map(fizbuzfunc, range(n))

fizzbuzz_materialized = compose(list)(gen_fizz_buzz)

gen_hex_fizz_buzz = compose(hexit)(fizzbuzz)
gen_hex_fizz_buzz(10)

dictionary_fizzbuzz = {
        i: gen_fizz_buzz(i) for i in range(100)
        }
dictionary_fizzbuzz[0].gent('0')

def fizzbuzz_imperative(n):
    l = []
    for i in range(n):
        output = ''
        if i % 3 == 0:
            output += 'fizz'
        if i % 5 == 0:
            output += 'buzz'
        yield output if len(output) > 1 else i
list(fizzbuzz_imperative(10))



from pampy import match, _

class spec(T):
    id = compose(StringField)(mapping)


inc = 0

update_inc = lambda x: globals().get(x)
multi_line = lambda x: ( inc+= 1 if x > 1 else multi_line(x + 1) )
multi_line(-5)


##############
#
# Raise errors from within lambdas
#
########

err = lambda x : TypeError("What is this") if x < 0 else x
err(-1)

######
#
# Polymorphism pattern matching using pampy
#
#####
from pampy import match, _

fib = lambda n: match(n,
         1,1,
         2,1,
         _, lambda x: fib(x-1) + fib(x - 2),
         )


########################################
#
# Pampi nested
#
########################################


match_inner = lambda x: match(x,
        2, lambda x: 'small',
        _, lambda x:  'big',
    )

match_outer = lambda x: match(x,
        is_div(3), lambda x: 'thrics'
        is_div(2), match_inner,
    )
match_outer(4)

###############
#
# Can we save functions in a file
#
###############

import pickle


def is_div_func(div):
    def do_div(n):
        return n % div == 0
    return do_div

pickle.dumps(is_div_func(2))

######
#
# Data classes
#
#####

from dataclasses import dataclass

@dataclass
class Student:
    id: int
    name: str

    @property
    def fizzbuzz(self):
        return fizzbuzz(self.id)
    @property
    def fizzbuzz_hex(self):
        return fizzbuzz_hex(self.id)


s1 = Student(id=1, name='My name is')

dict(**s1)


######
#
# All and break computations
#
#####



import time

slow_computation = lambda x: (time.sleep(2), print("wait"), x == 1)[2]
slow_computation(2)

all(map(slow_computation, [0] * 5))

any(map(slow_computation, [1] * 5))


