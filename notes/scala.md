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
