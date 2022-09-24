from math import *
key = {1:"+" , 2:"-" , 3:"*" , 4:"/" , 5:"^" , 6:"%" , "+":'1' , "-":'2' , "*":'3' , "/":'4' , "^":'5' , "%":'6'}
num1 = input("numper1 :")
num1 = int(num1)
num2 = input("numper2 :")
num2 = int(num2)
print("Keys : (1_ +)"
"(2_ -)"
"(3_ *)"
"(4_ /)"
"(5_ ^)"
"(6_ %)")
sum = num1 + num2
sub = num1 - num2
mul = num1 * num2
div = num1 / num2
squ = num1 ^ num2
rd  = num1 % num2

y_key = input("inter the key :")

if y_key == key[1] or y_key == key["+"]:
        print("Result = ",end="")
        print(sum,end="")
if y_key == key[2] or y_key == key["-"]:
        print("Result = ",end="")
        print(sub,end="")
if y_key == key[3] or y_key == key["*"]:
        print("Result = ",end="")
        print(mul,end="")
if y_key == key[4] or y_key == key["/"]:
        print("Result = ",end="")
        print(div,end="")
if y_key == key[5] or y_key == key["^"]:
        print("Result = ",end="")
        print(squ,end="")
if y_key == key[6] or y_key == key["%"]:
        print("Result = ",end="")
        print(rd,end="")
choi = {"1_ تقريب لأعلى رقم":"1" , "2_ أخذ الرقم بدون فاصلة عشرية":"2" , "3_ الخروج":"3"}

print()
print()
print("Other choices for result :")
print("1_ تقريب لأعلى رقم.")
print("2_ أخذ الرقم بدون فاصلة عشرية.")
print("3_ الخروج.")
print()
y_choi = input("inter your choice : ")
print()
from math import *

if (y_key == key[1] or y_key == key["+"]) and y_choi == choi["1_ تقريب لأعلى رقم"]:
         print("ceil the result = ", end="")
         print(ceil(sum), end="")
elif (y_key == key[1] or y_key == key["+"]) and y_choi == choi["2_ أخذ الرقم بدون فاصلة عشرية"]:
         print("floor the result = ", end="")
         print(floor(sum), end="")
else:
        if y_choi == choi["3_ الخروج"]:
                print("exit")


if (y_key == key[2] or y_key == key["-"]) and y_choi == choi["1_ تقريب لأعلى رقم"]:
        print("ceil the result = ", end="")
        print(ceil(sub), end="")
elif (y_key == key[2] or y_key == key["-"]) and y_choi == choi["2_ أخذ الرقم بدون فاصلة عشرية"]:
        print("floor the result = ", end="")
        print(floor(sub), end="")
else:
        if y_choi == choi["3_ الخروج"]:
                print("exit")


if (y_key == key[3] or y_key == key["*"]) and y_choi == choi["1_ تقريب لأعلى رقم"]:
        print("ceil the result = ", end="")
        print(ceil(mul), end="")
elif (y_key == key[3] or y_key == key["*"]) and y_choi == choi["2_ أخذ الرقم بدون فاصلة عشرية"]:
        print("floor the result = ", end="")
        print(floor(mul), end="")
else:
        if y_choi == choi["3_ الخروج"]:
                print("exit")

if (y_key == key[4] or y_key == key["/"]) and y_choi == choi["1_ تقريب لأعلى رقم"]:
        print("ceil the result = ", end="")
        print(ceil(div), end="")
elif (y_key == key[4] or y_key == key["/"]) and y_choi == choi["2_ أخذ الرقم بدون فاصلة عشرية"]:
        print("floor the result = ", end="")
        print(floor(div), end="")
else:
        if y_choi == choi["3_ الخروج"]:
                print("exit")

if (y_key == key[5] or y_key == key["*"]) and y_choi == choi["1_ تقريب لأعلى رقم"]:
        print("ceil the result = ", end="")
        print(ceil(squ), end="")
elif (y_key == key[5] or y_key == key["*"]) and y_choi == choi["2_ أخذ الرقم بدون فاصلة عشرية"]:
        print("floor the result = ", end="")
        print(floor(squ), end="")
else:
        if y_choi == choi["3_ الخروج"]:
                print("exit")

if (y_key == key[6] or y_key == key["%"]) and y_choi == choi["1_ تقريب لأعلى رقم"]:
        print("ceil the result = ", end="")
        print(ceil(rd), end="")
elif (y_key == key[6] or y_key == key["%"]) and y_choi == choi["2_ أخذ الرقم بدون فاصلة عشرية"]:
        print("floor the result = ", end="")
        print(floor(rd), end="")
else:
        if y_choi == choi["3_ الخروج"]:
                print("exit")