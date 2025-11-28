# Python Operators

- Operators are used to perform operations on variables and values.

# Arithmetic Operators

- ### Arithmetic operators are used with numeric values to perform common mathematical operations:

        +	Addition	x + y

         -	Subtraction	x - y

        *	Multiplication	x * y

        /	Division	x / y

        Division in Python
       Python has two division operators:
       / - Division (returns a float)
       // - Floor division (returns an integer)

      %	Modulus	x % y

      *.*	Exponentiation	x ** y

      //	Floor division	x // y

# Assignment Operators

- Assignment operators are used to assign values to variables:

        Operator Exp.   Same As
        =            x = 5     x = 5
        +=         x += 3   x = x + 3
        -=          x -= 3   x = x - 3
        /=          x /= 3    x = x / 3
        %=        x %= 3   x = x % 3
        //=       x //= 3   x = x // 3
        **=    x **= 3    x = x \*\* 3
        ^=       x ^= 3      x = x ^ 3

       The Walrus Operator
       Python 3.8 introduced the := operator, known as the "walrus operator". It assigns values to variables as part of a larger
       expression: > > :=
        print(x := 3) x = 3 > > print(x)

# Comparison Operators

- Comparison operators are used to compare two values:

### Equal x == y

### != Not equal x != y

### > Greater than x > y

### < Less than x < y

### Greater than or equal to x >= y

### Less than or equal to x <= y

> ### Comparison operators return True or False based on the comparison:

# Logical Operators

- ## Logical operators are used to combine conditional statements:

- > and Returns True if both statements are true x < 5 and x < 10

- > or Returns True if one of the statements is true x < 5 or x < 4

- > not Reverse the result, returns False if the result is true not(x < 5 and x < 10)

- # Identity Operators

- Identity operators are used to compare the objects, not if they are equal, but if they are actually the same object, with the same memory location:

> is Returns True if both variables are the same object x is y

- > is - Checks if both variables point to the same object in memory
- > == - Checks if the values of both variables are equal

> The is not operator returns True if both variables do not point to the same object:

# Membership Operators

- Membership operators are used to test if a sequence is presented in an object

> in => Returns True if a sequence with the specified value is present in the object x in y

> not => in Returns True if a sequence with the specified value is not present in the object

> Example : Get your own Python Server
> Check if "banana" is present in a list:fruits = ["apple", "banana", "cherry"]
> print("banana" in fruits)

## Operator Precedence

- Operator precedence describes the order in which operations are performed.

  - Parentheses has the highest precedence, meaning that expressions inside parentheses must be evaluated first:

    - print((6 + 3) - (6 + 3))

- Multiplication \* has higher precedence than addition +, and therefore multiplications are evaluated before additions:
