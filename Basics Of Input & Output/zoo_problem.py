'''
You are required to enter a word that consists of  and  that denote the number of Zs and Os respectively. 
The input word is considered similar to word zoo if . 2x = y

Determine if the entered word is similar to word zoo.

For example, words such as zzoooo and zzzoooooo are similar to word zoo but not the words such as zzooo and zzzooooo.

Input format

First line: A word that starts with several Zs and continues by several Os.
Note: The maximum length of this word must be .
Output format

Print Yes if the input word can be considered as the string zoo otherwise, print No.

SAMPLE INPUT 
zzzoooooo
SAMPLE OUTPUT 
Yes
'''

#string = "zzzzooooooooo"
string = input()
z = 0
o = 0

upto_z = string.find("o")

for i in range(upto_z):
    if ord(string[i]) != 122:
        break
    z += 1
    
for i in range(upto_z,len(string)):
    if ord(string[i]) != 111:
        break
    o += 1
    
if z == upto_z and o == (len(string) - upto_z) and len(string) == z + o and o == 2*z:
    print("Yes")
else:
    print("No")
