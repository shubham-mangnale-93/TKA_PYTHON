# ============================================================
#                 BITWISE OPERATORS IN PYTHON
# ============================================================

# Definition:
# Bitwise operators are used to perform operations on the individual bits of numbers.
# Python provides the following bitwise operators:
# &   -> Bitwise AND
# |   -> Bitwise OR
# ^   -> Bitwise XOR
# ~   -> Bitwise NOT
# <<  -> Left Shift
# >>  -> Right Shift


# ============================================================
# 1. BITWISE AND (&)
# ============================================================

# Bitwise AND returns 1 only when both corresponding bits are 1.

a = 5
b = 3

result = a & b

print("Bitwise AND:", result)


# ============================================================
# 2. BITWISE OR (|)
# ============================================================

# Bitwise OR returns 1 if at least one corresponding bit is 1.

a = 5
b = 3

result = a | b

print("Bitwise OR:", result)


# ============================================================
# 3. BITWISE XOR (^)
# ============================================================

# Bitwise XOR returns 1 when the corresponding bits are different.

a = 5
b = 3

result = a ^ b

print("Bitwise XOR:", result)


# ============================================================
# 4. BITWISE NOT (~)
# ============================================================

# Bitwise NOT reverses the bits of a number.
# 0 becomes 1 and 1 becomes 0.

a = 5

result = ~a

print("Bitwise NOT:", result)


# ============================================================
# 5. LEFT SHIFT (<<)
# ============================================================

# Left shift moves the bits to the left.
# Each left shift by 1 position is equivalent to multiplying by 2.

a = 5

result = a << 1

print("Left Shift:", result)


# ============================================================
# 6. RIGHT SHIFT (>>)
# ============================================================

# Right shift moves the bits to the right.
# Each right shift by 1 position is similar to integer division by 2.

a = 5

result = a >> 1

print("Right Shift:", result)

