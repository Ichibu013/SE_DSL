
s = input("Enter your string:")
l =[]
l = s.split()
print('Choices of actions that cah be performed:-')
print('\t1]Find the longest length in the string\n\t2]Occurance of a particular charcter is string')
print('\t3]Check if palindrome\n\t4]Index of substring\n\t5]Count of each word')
chi = int(input("Please enter the choice number:"))


def longlen(l):
    w =[]
    for i in l:
        if len(w)<len(i):
            w = i
    print(w,'is the longest word in the string')
    

def occurance(l):
    o = input("Enter the word to be seacrched:")
    c = 0
    for i in l:
        if i == o:
            c = c+1
    print(o,"repeats",c,"times")
    

def palindrome(s):
    p = s[::-1]
    if p == s:
        print("Entered string is a palindrome")
    else:
        print("Entered string is not a palindrone")
    

def substr(s):
    sub = input("Enter your substring:")
    print('Index of ',sub,'is',s.index(sub))
    

def count(l):
    k = list(dict.fromkeys(l))
    for i in range(len(k)):
        print(F"'{l[i]}' repeats",l.count(l[i]))


if chi==1:
    longlen(l)
elif chi ==2:
    occurance(l)
elif chi==3:
    palindrome(s)
elif chi==4:
    substr(s)
elif chi==5:
    count(l)
else:
    print('Entered choice number is invalid')
