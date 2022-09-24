# 1_ Display numbers from a list using a loop

numbers = [12, 75, 150, 180, 145, 525, 50]
result = [ ]
for item in numbers :
    if item > 500:
      break
    if item % 5 == 0 and item <= 150:
        result.append(item)

print(result)

