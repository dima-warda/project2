numbers = [ ]
num1 = input("numper1 :")
num2 = input("numper2 :")
num3 = input("numper3 :")
num4 = input("numper4 :")
num5 = input("numper5 :")

numbers.append(num1)
numbers.append(num2)
numbers.append(num3)
numbers.append(num4)
numbers.append(num5)

numbers.sort()

print(numbers)
print(numbers[0], max(numbers))
