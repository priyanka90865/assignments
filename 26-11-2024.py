#1. Python Program to count occurrence of a given characters in string. 

str=input("Enter a word or sentence: ")
l=list(str)
#print(l)
freq=[l.count(ele) for ele in l]
#print(freq)
d= dict(zip(l,freq))
print(d)


#2. Python Program to check if two Strings are Anagram. 

str1=input("Enter a string1: ")
str2=input("Enter a string2: ")
if len(str1)!=len(str2):
    print("Not Anagram")
else:
    if sorted(str1) == sorted(str2):
        print("strings are Anagram")
    else:
        print("Not Anagram")


#3. Python program to check a String is palindrome or not. 

sp=input("Enter a string: ")
revstr=(sp[::-1])
if revstr==sp:
    print("string is palindrome")
else:
    print("string is not palindrome")

#4. Python program to replace the string space with a given character. 

s="python"
c= "open source program"
s1=" "
for i in s:
    if i==" ":
        s1+=c
    else:
        s1 += i
print("string: ",s1)

