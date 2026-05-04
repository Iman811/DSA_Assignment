car={"name":"maruti","model": 2561,"year":2026}
car["colour"]="red"
car["year"]=2024
#print(car)
if "price" in car:
     print("Price is present")
else:
     print("Price is not present")
print("================================================")
print(car.pop("year"))
print("================================================")
del(car["colour"])
print("================================================")
print(car)
print("================================================")

for key in car:
     print(key)
print("================================================")

for key in car.values():
     print(key)
print("================================================")

keys = ["name", "age", "job"] 
values = ["Alice", 25, "Dev"]
new_dict=dict(zip(keys,values))
print(new_dict)
print("================================================")

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}
merged = dict1 | dict2
new = {**dict1, **dict2}
print(merged)
print(new)
print("================================================")

# Write a program to count the number of occurrences of each character in the string "hello" using a dictionary.
text = "hello"   
counts = {}

for char in text:
    if char in counts:
        counts[char] += 1  # Increment if already there
    else:
        counts[char] = 1   # Add new key with value 1

print(counts)


# Write a program to count the number of occurrences of vowels in the string  using a dictionary.
text = "doeuleia,"   
counts = {}
vowel='aeiouAEIOU'

for char in vowel:
    if char in counts:
        counts[char] += 1  # Increment if already there
    else:
        counts[char] = 1   # Add new key with value 1

print(counts)