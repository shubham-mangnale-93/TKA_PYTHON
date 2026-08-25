import math
print(math.sqrt(81))        # 9.0 — square root
print(math.factorial(5))    # 120 — 5! = 5×4×3×2×1
print(math.isqrt(81))       # 9 — integer square root
print(math.lcm(14, 36))     # 252 — least common multiple
print(math.gcd(14, 36))     # 2 — greatest common divisor
#----------------------------------------------------------------


from datetime import datetime
dt1 = datetime(2026, 4, 12, 12, 15, 00)  # April 12, 2026, 12:15:00
print(dt1)          # 2026-04-12 12:15:00
print(dt1.date())   # 2026-04-12
print(dt1.time())   # 12:15:00
print(dt1.year)     # 2026
print(dt1.month)    # 4
print(datetime.today())  # current date and time

today = datetime.today()
print(today.year)   # 2026
print(today.month)  # 8
print(today.day)    # 20

today = datetime.today()
print(today.weekday())         # 3  (Monday=0 ... Sunday=6)
print(today.isoweekday())      # 4  (Monday=1 ... Sunday=7)
print(today.strftime("%A"))    # Thursday
print(today.isocalendar()[1])  # ISO week number of the year
#----------------------------------------------------------------



