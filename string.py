# slicing 
"""name='Imanarafat'
print(name)
print(name[:3])     
print(name[1:3])
print(name[1:])
print(name[:3:-1]) 
  # : (Start - Empty): Because the start position is empty, it means "start from the very end" (since the step is negative).
  # :3 (Stop - 3): This means "stop before index 3". It tells Python to stop slicing when it reaches index 3 (the 4th character).
  # :-1 (Step - -1): This tells Python to move backward, one character at a time.


print(name[:3:1]) # I,m,a"""


"""for i in name:
    print(i,)
    print(i,end=' ')"""


"""j=name.replace('a','aa')
print(j)
print(len(name))
print(name.upper())
print(name.lower())
print(name.strip())
print(name+surname)"""

"""name="iman  "
surname="arafat"
print(f"My name is {name} my surname is{surname}") #formating value 'f' is used"""


## Practice Question

"""#1
name='Iman'
print(name[::-1])

#2
print(len(name))"""""

"""#3 number of character count
name='Imaan'
count=0
new={}
for i in name:
    if i in new:
        new[i]+=1
    else:
        new[i]=1
print(new)"""

"""#4  Palindrom
word=input("Enter the word  ")
new=(word[::-1])
if word == new:
    print(f"It is a palindrom {word}:{new}") 
else:
    print(f"It is not a palindrom {word}:{new}")"""

## what is the diferents between 'in' and '==' . because when is used 'in' to check whether a word is palindrom or not i, got it is not a palindrom but when i used '==' i got a correct output.


"""#5 vowel count
word='mississippi'
vowel='aeiouAEIOU'
count=0
for i in word:
    if i in vowel:
        count+=1
print(count)"""

#6 remove dublicate items
