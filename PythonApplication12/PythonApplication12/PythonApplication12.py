numbers = [1,10,5,16,4,9,10]
letters = ['a','g','s','b','y','a','s']

val = min(numbers)
val2 = max(numbers)
val3 = max(letters)
val4 = min(letters)
val5 = numbers[3:6]
val6 = numbers[:3]
val7 = numbers[4:]

print(val)
print(val2)
print(val3)
print(val4)
print(val5)
print(val6)
print(val7)

numbers[4] = 40
print(numbers)

numbers.append(49)
print(numbers)

numbers.append(59)
print(numbers)

numbers.insert(3,89)
print(numbers)

numbers.insert(-1,52)
print(numbers)

numbers.pop(0)
print(numbers)

numbers.pop(-1)
print(numbers)

numbers.remove(89)
print(numbers)

numbers.sort()
print(numbers)

letters.sort()
print(letters)

letters.reverse()
print(letters)

numbers.clear()
print(numbers)

print(numbers.count(10))
print(letters.count('a'))