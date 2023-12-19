
def square(num): return num ** 2

result = square(5)
print(result)


numbers = [1,3,5,9]
result = list(map(square, numbers))
print(result)

for item in map(square, numbers):
    print(item)



numbers = [1,3,5,9]
result = list(map(lambda num: num ** 2,numbers))
print(result)



square = lambda num: num ** 2
numbers = [1,3,5,9]
result = square(3)
print(result)



numbers = [1,3,5,9,10,4]
def check_even(num): return num%2==0
result = list(filter(check_even,numbers))
print(result)


result = list(filter(lambda num: num%2==0,numbers))
print(result)


check_even = lambda num: num%2==0
result = check_even(numbers[2])
result2 = check_even(numbers[5])
print(result)
print(result2)