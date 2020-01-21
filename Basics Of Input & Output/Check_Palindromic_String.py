'''
You have been given a String S. You need to find and print whether this string is a palindrome or not. If yes, print "YES" (without quotes), else print "NO" (without quotes).

Input Format
The first and only line of input contains the String S. The String shall consist of lowercase English alphabets only.

Output Format
Print the required answer on a single line.

Constraints: 1<= |S| <= 100

Note
String S consists of lowercase English Alphabets only.

SAMPLE INPUT 
aba
SAMPLE OUTPUT 
YES
'''

n = input()
arr = 0
for i in range(int(len(n)/2)+1):
    if n[i] == n[-i-1]:
        arr +=1
        #print("match")
    else:
        break

if len(n)%2 == 0:
    arr -= 1
    
print(arr)
if len(n)%2 == 0 and arr == int(len(n)/2):
    print("Palindrome")
elif len(n)%2 == 1 and arr == int(len(n)/2) + 1:
    print("Palindrome")
else:
    print("Not Palindrome")

