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



