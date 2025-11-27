# Python Numbers

### There are three numeric types in Python:

    int
    float
    complex

### Variables of numeric types are created when you assign a value to them:

# Example

    x = 1    # int
    y = 2.8  # float
    z = 1j   # complex

## imp: To verify the type of any object in Python, use the type() function:

      print(type(x))
      print(type(y))
      print(type(z))

## Int

- Int, or integer, is a whole number, positive or negative, without decimals, of unlimited length.

## Float

- Float, or "floating point number" is a number, positive or negative, containing one or more decimals.

## Complex

- Complex numbers are written with a "j" as the imaginary part:

## Type Conversion

- You can convert from one type to another with the

      int(),
      float(),
      and complex() methods:
      x = 1 # int
      y = 2.8 # float
      z = 1j # complex
      #convert from int to float:
      a = float(x)
      #convert from float to int:
      b = int(y)
      #convert from int to complex:
      c = complex(x)
      -  print(a)
      -  print(b)
       - print(c)
      print(type(a))
      print(type(b))
      print(type(c))

## Random Number : Python does not have a random() function to make a random number, but Python has a built-in module called random that can be used to make random numbers:

    import random
    print(random.randrange(1, 10))
