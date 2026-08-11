'''
Challenging Dictionary Tasks
'''
# 41. Merge two dictionaries without using the | operator.
d1 = {"a": 1, "b": 2}
d2 = {"b": 3, "c": 4}
merged = d1.copy()
merged.update(d2)
print("41.",merged)
#--------------------------------------------------------------------------------------------------

# 42. Find common keys between two dictionaries.
common_keys = d1.keys() & d2.keys()
print("42.",common_keys)
#--------------------------------------------------------------------------------------------------

# 43. Find keys present in the first dictionary but not in the second.
key = d1.keys()- d2.keys()
print("43.",key)
#--------------------------------------------------------------------------------------------------

# 44. Create a dictionary from two separate lists: one containing keys and another containing values.
keys_list = ["id", "name", "price"]
values_list = ["P101", "Laptop", 55000]
list_dict = dict(zip(keys_list, values_list))
print("44.", list_dict)
#--------------------------------------------------------------------------------------------------

# 45. Reverse a dictionary so that values become keys and keys become values.
original = {"a": 1, "b": 2, "c": 3}
reversed_dict = {}                        
for k, v in original.items():            
    reversed_dict[v] = k               
print("45.",reversed_dict)
#--------------------------------------------------------------------------------------------------

# 46. Count the frequency of every character in a user-given string using a dictionary.
s = "hello"
freq = {}

for ch in s:
    if ch in freq:
        freq[ch] = freq[ch] + 1
    else:
        freq[ch] = 1
print("46.",freq)
#--------------------------------------------------------------------------------------------------

# 47. Count the frequency of every word in a sentence.
sentence = "python is easy and python is powerful"
words = sentence.split()
word_freq = {}

for word in words:
    if word in word_freq:
        word_freq[word] = word_freq[word] + 1
    else:
        word_freq[word] = 1
print("47.",word_freq)
#--------------------------------------------------------------------------------------------------

# 48. Group student names by their city using a dictionary.
students = [
    ("Kunal", "Pune"),
    ("Pavan", "Mumbai"),
    ("Sneha", "Pune"),
    ("Rahul", "Mumbai"),
    ("Anita", "Nashik")
]

city_groups = {}
for name, city in students:
    if city in city_groups:
        city_groups[city].append(name)
    else:
        city_groups[city] = [name]
print("48.",city_groups)
#--------------------------------------------------------------------------------------------------

# 49. Sort a dictionary by its values in ascending order.
marks = {"Kunal": 78, "Pavan": 92, "Sneha": 65, "Rahul": 85}
sorted_marks = dict(sorted(marks.items(), key=lambda item: item[1]))
print("49.",sorted_marks)
#--------------------------------------------------------------------------------------------------

# 50. Remove duplicate values from a dictionary while keeping the first matching key.
data = {"a": 1, "b": 2, "c": 1, "d": 3, "e": 2}
seen_values = set()
unique_dict = {}

for key, value in data.items():
    if value not in seen_values:
        unique_dict[key] = value
        seen_values.add(value)
print("50.",unique_dict)
#--------------------------------------------------------------------------------------------------
