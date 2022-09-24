# 3_Reverse a given integer number

number = 76542
num_resl = 0
while number > 0 :
    rev = number %10
    num_resl = num_resl * 10 + rev
    number = number //10
print(num_resl)

