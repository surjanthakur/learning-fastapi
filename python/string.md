# all about string

- Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello' is the same as "hello".

### You can display a string literal with the - print("Hello") function:

# Slicing

- You can return a range of characters by using the slice syntax.

- Specify the start index and the end index, separated by a colon, to return a part of the string.
- b = "Hello, World!" print(b[2:5])

- # Negative Indexing

- Use negative indexes to start the slice from the end of the string:

Get the characters:
From: "o" in "World!" (position -5)
To, but not included: "d" in "World!" (position -2):

- b = "Hello, World!"
  print(b[-5:-2])

# Upper Case

- The upper() method returns the string in upper case:
  a = "Hello, World!"
  print(a.upper())

# Lower Case

- The lower() method returns the string in lower case:
  a = "Hello, World!"
  print(a.lower())

- # Remove Whitespace

- The strip() method removes any whitespace from the beginning or the end:
  a = " Hello, World! "
  print(a.strip()) # returns "Hello, World!"

# String Concatenation

- To concatenate, or combine, two strings you can use the + operator :

- a = "Hello"
  b = "World"
  c = a + b
  print(c)

- # String Format

- As we learned in the Python Variables chapter, we cannot combine strings and numbers.
- But we can combine strings and numbers by using f-strings or the format() method!

- # F-Strings

- F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.To specify a string as an f-string, simply put an f in front of the string literal, and add curly brackets {} as placeholders for variables and other operations.

- Example
  Create an f-string:
- age = 36
- txt = f"My name is John, I am {age}"
  print(txt)

# Python - String Methods

- ## capitalize() Converts the first character to upper case

  - The capitalize() method returns a string where the first character is upper case, and the rest is lower case.

    - txt = "hello, and welcome to my world."
    - x = txt.capitalize()
      print (x)

- ## casefold() Converts string into lower case

  - The casefold() method returns a string where all the characters are lower case.This method is similar to the lowermethod, but the casefold() method is stronger, more aggressive, meaning that it will convert more characters into lower case, and will find more matches when comparing two strings and both are converted using the casefold() method.
    - txt = "Hello, And Welcome To My World!"
    - x = txt.casefold()
    - print(x)

- ## count() Returns the number of times a specified value occurs in a string

  - The count() method returns the number of times a specified value appears in the string.
    - txt = "I love apples, apple are my favorite"
    - x = txt.count("apple")
    - print(x)

- ## find() Searches the string for a specified value and returns the position of where it was found

  - The find() method finds the first occurrence of the specified value.

  - The find() method returns -1 if the value is not found.The find() method is almost the same as the index() method, the only difference is that the index() method raises an exception if the value is not found. (See example below)
    - txt = "Hello, welcome to my world."
    - x = txt.find("welcome")
    - print(x)

- ## index() Searches the string for a specified value and returns the position of where it was found
  - The index() method finds the first occurrence of the specified value.The index() method raises an exception if the value is not found.The index() method is almost the same as the find() method, the only difference is that the find() method returns -1 if the value is not found. (See example below)
    - txt = "Hello, welcome to my world."
    - x = txt.index("welcome")
    - print(x)
- ## join() Joins the elements of an iterable to the end of the string
  - The join() method takes all items in an iterable and joins them into one string.A string must be specified as the separator.
    - myTuple = ("John", "Peter", "Vicky")
    - x = "#".join(myTuple)
    - print(x)
- ## lower() Converts a string into lower case
  - The lower() method returns a string where all characters are lower case.
    Symbols and Numbers are ignored.
    - txt = "Hello my FRIENDS"
    - x = txt.lower()
    - print(x)
- ## replace() Returns a string where a specified value is replaced with a specified value
  - The replace() method replaces a specified phrase with another specified phrase.
    - txt = "I like bananas"
    - x = txt.replace("bananas", "apples") print(x)
- ## startswith() Returns true if the string starts with the specified value
  - The startswith() method returns True if the string starts with the specified value, otherwise False.
    - txt = "Hello, welcome to my world."
    - x = txt.startswith("Hello")
    - print(x)
- ## strip() Returns a trimmed version of the string
  - The strip() method removes any leading, and trailing whitespaces.
    Leading means at the beginning of the string, trailing means at the end.
    You can specify which character(s) to remove, if not, any whitespaces will be removed.
    - txt = " banana "
    - x = txt.strip()
    - print("of all fruits", x, "is my favorite")
- ## title() Converts the first character of each word to upper case
- ## swapcase() Swaps cases, lower case becomes upper case and vice versa
- ## upper() Converts a string into upper case
