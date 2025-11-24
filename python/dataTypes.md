# data types in python

# Integer

a = 10

print("Integer:", a, "Type:", type(a))

# Float

b = 10.5

print("Float:", b, "Type:", type(b))

# String

c = "Hello, World!"

print("String:", c, "Type:", type(c))

# Boolean

d = True

print("Boolean:", d, "Type:", type(d))

# List

e = [1, 2, 3, 4, 5]

print("List:", e, "Type:", type(e))

# Tuple

f = (1, 2, 3, 4, 5)

print("Tuple:", f, "Type:", type(f))

# Dictionary

g = {"name": "Alice", "age": 25}

print("Dictionary:", g, "Type:", type(g))

# Set

h = {1, 2, 3, 4, 5, 4, 3, 1}'

print("Set:", h, "Type:", type(h))

# NoneType

i = None

print("NoneType:", i, "Type:", type(i))

# Complex Number

j = 2 + 3j

print("Complex Number:", j, "Type:", type(j))

# Byte

k = b"Hello"

print("Byte:", k, "Type:", type(k))

# Bytearray

l = bytearray(5)

print("Bytearray:", l, "Type:", type(l))

# Frozenset

m = frozenset([1, 2, 3, 4, 5])

print("Frozenset:", m, "Type:", type(m))

# Range

n = range(5)

print("Range:", n, "Type:", type(n))

# Memoryview

o = memoryview(b"Hello")

print("Memoryview:", o, "Type:", type(o))

# Frozen Dictionary (using types.MappingProxyType)

import types

p = types.MappingProxyType({"key": "value"})
print("Frozen Dictionary:", p, "Type:", type(p))
