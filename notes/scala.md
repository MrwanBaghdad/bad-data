# The absolute noob's guide to scala 

## Operators and methods 
* Mathematical operators such as `+` and `-` are actually methods with a symbolic names 
> 1 + 2 == 1.+(2) 
* Evaluation happens from left to right, and it stops when the expression is reduced to a value 

## Difference between `val` and `def`: 
 * The right handside of `val` is _evaluated_ at point of definition and then is called by value 
 * The right handside of `def` is _evaluated_ every time when is called 
 
 ## Evalution of function applications: 
 Application of paramatrized functions are evaluated as operator experssions. 
 - Evaluate all function arguments, from left to right 
 - Evaluate function application, and replacing params with actual values 
 
 ## Evaluation models offered by scala: 
 ### non-strict evaluation Call by name
 Don't reduce the para expression until the function is called/needed 
 
 ```scala 
 sumOfSquares(3, 2 + 2)
square(3) + square(2 + 2)
3 * 3 + square(2 + 2)
9 + square(2 + 2)
9 + (2 + 2) * (2 + 2)
9 + 4 * (2 + 2)
9 + 4 * 4
25
```
### Strict evaluation call by value 
Reduce every param expression before apply the function application 
```scala
sumOfSquares(3, 4)
square(3) + square(4)
3 * 3 + square(4)
9 + square(4)
9 + 4 * 4
9 + 16
25
```

## Conditional expressions
Adding boolean logic to expression evaluations
```scala
def abs(x: Double) = if(x>=0) x else -x 
```
### Boolean operators 
```scala 
true  false      // Constants
!b               // Negation
b && b           // Conjunction
b || b           // Disjunction
```

## Recursive functions 
In scala, recursive functions needs their return type explicitly defined.
For non recursive methods, the return type is optional.

## Nested functions
Cutting functions into small blocks of other functions is good function programming practice. 
To get that and avoid _namespace pollution_ we should add the smaller steps into the main function context 
in other word _blocks_ `{...}`.

A block is delimited by braces `{...}`

### Blocks 

* A block is seires of definitions and expressions.
* Last element define its value i.e _it has a return value_ 

### Blocks and visibility 
>The definitions inside a block are only visible from within the block.
>The definitions inside a block shadow definitions of the same names outside the block.
Shadowing means that changes in the block are only scoped inside the block and not reflected outside the outer context.

### Semicolons and infix operators 
* Semicolons are optional 
* To write multiline expressions add the operator at the end of the line that point to the interpter 
that continue of the expression is still yet to come. 
```scala 
Expresson1+ 
Expression2 //Evaluated to one expression 

Expression1 
+ Expression2 //Evaluated to two expressions 
```
### Top level definitions 
Scala programms must be written within a top-level _object definition_ 
```scala
object MyExecutableProgram {
  val myVal = …
  def myMethod = …
}
```

## Recursive function application 
### Tail recursion 

The fibpnnaci seires implementation 
``scala
def fib(x: Int): Int = 
 if (x == 1) x else x * fib(x - 1)
 ``` 
 For fib(4) it's evaluated to 
 > 4 * (fib(3))
 > 4 * 3 * fib(2))
 > 4 * 3 * 2 * fib(1) 
 > 4 * 3 * 2 * 1 
 > 24 
 ```
 The recursion is at the _tail_ which is the most right hand side of the expression adding to the space 
 size of the evaluation to get contrasting this to 

 ```scala 
 def factorial(n: Int): Int = {
  @tailrec
  def iter(x: Int, result: Int): Int =
    if (x == 1) result
    else iter(x -  1, result * x)

  iter(n, 1)
}
 ```
 This will add the get the recursion to be not tail-recursive one. 

**By default all recursive functions are optimized to set that function is tail-recursive 
add the `@tailrec` to the method definition**


## Structuring information 
### Case classes 
A case class resembles a named tuple in python. It's used to encapsulate values within the same context or 
or derived from same context 

```scala 
case class Person(firstName: String, lastName: String, age: Int)
val person1 = Person("Marwan", "Nabil", 24)
person1.firstName // = "Marwan"
person1.age = 24 // = 24
```
### Sealed traits 

One could group classes using traits. A trait can be explained like a mash between 
enums and interfaces. 

* Sealed is just a modifier that's can be best explained that it mimics the `private` modifier in Java. 
Applying it to a trait that only objects defined in the same file can _extend_ that trait. 

So in above example we can define a trait called a `Being` which has an alternative - note the wording think of it as an enum - `Person`

```scala 
sealed trait Being 
case class Person( firstName: String, lastName: String, age: Int) extends Symbol 
case class Animal (petName: String, age: Name) extends Symbol 

val person1: Symbol = Person("Marwan", "Nabil", 23)
val animal1: Symnbol = Animal("Blue", 12)
```

### Pattern matching 

Pattern matching is method kind of a complicated (if-else) paradigm, we can use pattern matching to differentiate between:

* values 
```scala
def matchTest(x: Int): String = x match {
  case 1 => "one"
  case 2 => "two"
  case _ => "other"
}
matchTest(3)  // other
matchTest(1)  // one
```

* case classes
```scala
def symbolDuration(symbol: Symbol): String =
  symbol match {
    case Note(name, duration, octave) => duration
    case Rest(duration) => duration
  }
```
* types (classes)
```scala
abstract class Device
case class Phone(model: String) extends Device {
  def screenOff = "Turning screen off"
}
case class Computer(model: String) extends Device {
  def screenSaverOn = "Turning screen saver on..."
}

def goIdle(device: Device) = device match {
  case p: Phone => p.screenOff
  case c: Computer => c.screenSaverOn
}
```
* types with guards 
```scala
def showImportantNotification(notification: Notification, importantPeopleInfo: Seq[String]): String = {
  notification match {
    case Email(sender, _, _) if importantPeopleInfo.contains(sender) =>
      "You got an email from special someone!"
    case SMS(number, _) if importantPeopleInfo.contains(number) =>
      "You got an SMS from special someone!"
    case other =>
      showNotification(other) // nothing special, delegate to our original showNotification function
  }
}
```
### pattern mathcing with sealead traits 

Since a sealed trait can has all its _alternatives_ (definitions) in the same file. The compiler can 
detect non exhaustive _match blocks_. Allowing for a more safe pattern matching block. 

### Algebric data types 
```
Data types defined with sealed trait and case classes are called algebraic data types. 

An algebraic data type definition can be thought of as a set of possible values.
```
**If a concept of your program’s domain can be formulated in terms of an is relationship, you will express it with a sealed trait**

**On the other hand, if a concept of your program’s domain can be formulated in terms of an has relationship, you will express it with a case class:**


### Higher order functions 

Functional languages treats functions as first-class objects. That they can be defined without
being encapsulated in objects. _No need for the command pattern here_ 
One feature that you get from having functions defined as that that they can be passed to other 
functions and be used to return other functions _think function decorators_ 

Consider the following example,

```scala 
def sumInts(a: Int, b:Int): Int = 
 if ( a > b) 0 else a + sumInts(a + 1, b)
```
But what if we want to get the sum of cubes for a range between `a` and `b`

```scala
def cube(x: Int): Int = x*x*x 

def sumCubes(a: Int, b: Int): Int = 
 if (a > b) 0 else a + sumCubes(a + 1, b) 
```
The above code isn't very dry the same functionality can be expressed with using the `sumInts` using 
higher order functions. 

Refacoting the `sumInts` to accept a function to apply we need to define the function signature which
is a linear function that takes and return an integer 

```scala
def sum(f: Int => Int, a: Int, b: Int): Int =
 if (a > b) 0 else f(a) + sum(f, a+1, b) 
```
We can then re-write the `sumInts` and `sumCube` to be: 

```scala
def cube(x: Int): Int = x*x*x
def sumCube(a: Int, b:Int) = sum(cube, a, b)

def id(x: Int): Int = x 
def sumInts(a: Int, b:Int) = sum(id, a, b)

```

### Anonymous functions 

* Anonymous functions syntax: 
 ```scala 
 (x :Int) => x * x * x
 ```

Creating and naming small lambda functions can be tedious to overcome this 
we can use then anonymous functions to re-write the above 

```scala 
def sumCubes(a: Int, b: Int) = sum(x => x * x * x, a, b)
def sumInts(a: Int, b: Int) = sum(x => x, a, b)
```

### Standard library 

#### Lists 

In scala lists are homogenous, recursive and immutable

```scala 
val fruits: List[String] = List("apple", "oranges", "pears")
val nums = List(1, 2, 3, 4)
val diag3: List[List[Int]] = List(List(1, 0, 0), List(0, 1, 0), List(0, 0, 1))
```
Lists are all a composed from the empty list `Nil` 

```scala 
val emptyList1 = List()
val emptyList2 = Nil 
```

Lists are composed using cons `::` `x :: xs` gives a new list with first element `x` 
cons assossiate to the right. thus

Example

```scala 
val fruits = "oranges" :: "apples" :: "pears" :: Nil 
val fruits = Nil.::("pears").::("apples").::("oranges")
```

* Pattern matching on lists:
 
 ```scala
 nums match {
  // Lists of `Int` that starts with `1` and then `2`
  case 1 :: 2 :: xs => …
  
  // Lists of length 1
  case x :: Nil => …
  
  // Same as `x :: Nil`
  case List(x) => …
  
  // The empty list, same as `Nil`
  case List() =>
  
  // A list that contains as only element another list that starts with `2`
  case List(2 :: xs) => …
}
```
 
 #### Common operations on list 
 
`map`, `filter` and `flatMap`
 
```scala 
//map 
List(1, 2, 3).map( x => x + 1) == List(2, 3, 4)
 
//filter 
List(1, 2, 3).filter( x => x % 2 == 0 ) == List(2) 
 
//flatMap: transfomr each element into a list and aggregate and finally flaten 

val xs = 
List(1, 2, 3).flatMap { x => 
 List(x, 2 * x, 3 * x)
 
 xs == List(1, 2, 3, 2, 4, 6, 3, 6 , 9) 
 
```

