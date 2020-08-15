
identity = lambda x: x
I = identity
identity(1)

const = lambda x: lambda y: x
const(4)(2)

# Mocking bird self applicaton of self application

M = lambda f: f(f)
M(identity)(2)


#kerstal choose the first argument also named the conse in Haskell

K = lambda a : lambda b : a
K(1)(2) # == 1
K(2)(1) # == 2


# Kite choose the second argument
KI = lambda x: lambda y: y
KI(1)(2)

## Another way to write kite is using Identity function
KI = lambda x: identity
KI(2)(3)


## Cardinal takes a function and two argument and flip the two arguments

C = Cardinal = lambda f : lambda a : lambda b : f(b)(a)
C(K)(I)(M)


############################################
#
# Boolean and Boolean logic
#
############################################

# What's a boolean used for selection
# result := bool exp1 exp2
# result := func arg1 arg2 That's because arg1 and arg2 are also functions (expression?)

true = K
false = KI
true.__str__ = 'True/ K'
false.__str__ = 'False / KI'


And = lambda p: lambda q: p(q)(p)
And(true)(false) == false

Or = lambda p: lambda q: p(p)(q)

## Composition bluebird AKA piping
Compose = lambda f : lambda g : lambda a: f(g(a))


## Data structures
pair = lambda a : lambda b: lambda f: f(a)(b)
pair(2)(3)(K)



##########################################################################################
#
#
#   DESIGN PATTERNS IN functional programming
#
##########################################################################################



# Partial functions

'''
Partial functions is the first principle to get compositions. Thinking within the OOP framework Composition is usually better for code
sharing and encabsulating functionality that being motivated by the SOLID principles, particulary the Interface segregation and Single responsibility
A direct consequence of the previous motivation in the OOP space is the strategy pattern.
In strategy pattern, we're motivated to use interfaces and concerete classes that acheive a single responsibility
But what if we have an interface that can define a single method?

Interface Additive:
    public int add(x: int, y: int)

Interface Subtracable:
    public int sub(int x, int y)

In the functional sense we can look at single method interfaces as function __types__. As they allow for enforcing signatures at compile time
And allow of managing functions as objects through concrete classes that implement them.
In functional languages, we don't need to manage these basic blocks; Functions are first class citizens that means they're objects or more
concretly defined as values. In python and JS for examples, you can use the lambda functions (python) and Anonymous functions in JS to
intialize function definitions and also (bind) them to variables and constants. Which allows them to handle them as objects values. In python and JS for examples, you can use the lambda functions (python) and Anonymous functions in JS to

e.g
Python: add = lambda x, y: x + y
JS: add = (x,y) => x + y

Allowing functions to be handled as values allow them to be passed to other functions. SAY WHAT!?

'''

def do_thing(action, name):
    print("Hello my name is %s" % name)

say_name = lambda x: "hello my name is %s" % x
print_it = lambda s: print(s)
print_name = compose(print_it)(say_name)
# print_name = lambda name: print_it(say_name(name))
print_name("marwan")

yell_name = compose(print_name)(lambda s: s.upper())
yell_name("Marwan")


#######
#
# How to code with options
#
#####

add42 = lambda x : x + 42
def map_option(func):
    def wrapped(*args, **kwargs):
        try:
            return (func(*args, **kwargs), None)
        except Exception as err:
            return (None, err)
    return wrapped

add42_to_option = map_option(add42)
add42_to_option('2')

from pampy import match, Any


add42 = lambda x : x + 42 if isinstance(x, int) else None

bind = lambda f: lambda v: match(v,
        None, None,
        _, lambda x: f(v),
        )

tohex = lambda v: hex(v)
jipe = compose(bind(tohex))(bind(add42))
pipe('3334')

#compose = lambda f: lambda g: lambda v: f(g(v))



infc = lambda v: lambda f: compose(f)(v)
f = compose(add42)(lambda x: x - 2)
f(2)


###########
#
# What are monads?
#
##########

import math



sine = lambda x: math.sin(x)
cube = lambda x: x ** 3
sine_cubed = compose(cube)(sine)
sine_cubed(3)

sine_logging = lambda x, log : (math.sin(x), log + 'sin was called')
sine_logging(1,'')

cube_logging = lambda x, log : ( x**3, log + 'cube was called' )
cube_logging(3,'')

cube_logging(*sine_logging(1,''))

sine_cubed_with_logging = compose(cube_logging)(sine_logging)

sine_cubed_with_logging(2, '')

#Monad: Unit
# logged = lambda msg: lambda f: lambda x : (f(x), msg)
# sine_logged = logged('sin was called')(sine)
# sine_logged(2)
unit = lambda v: (v, '')

#Monad: Bind

def bind(monad_val, transform):
    #unwrap
    (val, msg) = monad_val
    result, updates = transform(val)
    return (result, msg + ' ' + updates)
#
f0 = bind(unit(2), logged("sine is called")(sine))
bind(f0, logged('cube is called')(cube))

unit(2).
    bind(logged('sine is called')(sine)).
    bind(logged('cube is called')(cube)).


@dataclass
class Writer:
    val: int
    log: str
    def bind(self, transform):
        val, log = self.val, self.log
        res, updates = transform(val)
        return Writer(res, log + ' ' + updates)

clear_log = lambda writer: Unit(writer.val)

Unit(2)

sine_cube_logged = lambda x: (x.\
    bind(logged('sine is called')(sine)).\
    bind(logged('cube is called')(cube)))

sine_cube_logged(Unit(2))

extract_val = lambda monad: monad.val
sine_cube_int = compose(extract_val)(sine_cube_logged)

