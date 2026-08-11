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
#---------------------------------------------------------------------------------------------------

"""
Bitwise Operators - Explained

a = 5   -> binary: 0101
b = 3   -> binary: 0011


1. & (AND) - Result bit is 1 only if both bits are 1

    0101
    0011
    ----
    0001  -> 1


2. | (OR) - Result bit is 1 if either bit is 1

    0101
    0011
    ----
    0111  -> 7


3. ^ (XOR) - Result bit is 1 only if the two bits are different (same bits give 0)

    0101
    0011
    ----
    0110  -> 6


4. ~ (NOT) - Flips every bit (0->1, 1->0). In Python, the formula is: ~a = -(a+1)
    ~5 = -(5+1) = -6


5. << (Left Shift) - Bits move to the left, which means x 2 for every shift
    5 << 1  ->  5 x 2 = 10

    Bit-level view:
    Before:   0 1 0 1     (this is 5)
    Shifted left by 1:
    After:    1 0 1 0     (this is 10)
    A new 0 is added at the end, and every bit moves one position left.


6. >> (Right Shift) - Bits move to the right, which means / 2 for every shift
   (the remainder/decimal part is dropped)

    5 >> 1  ->  5 / 2 = 2 (decimal part dropped)

    Bit-level view:
    Before:   0 1 0 1     (this is 5)
    Shifted right by 1, last bit '1' is dropped:
    After:    0 0 1 0     (this is 2)
    The last bit is lost, and the rest of the bits shift right.


In short:
- << (left shift)  = multiplies the number by 2 (for each shift)
- >> (right shift) = divides the number by 2, dropping the remainder (for each shift)
"""
