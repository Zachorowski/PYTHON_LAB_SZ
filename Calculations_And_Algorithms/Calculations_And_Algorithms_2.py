from random import randint

numbers = []
numbers_length = 50

for i in range(numbers_length):
    numbers.append(randint(0,50))

def sort(list):
    for j in range(len(list)-1):
        for i in range(len(list)-1):
            if (list[i]>list[i+1]):
                list[i],list[i+1]= list[i+1], list[i]

print(numbers)
sort(numbers)
print(numbers)
numbers.sort()
print(numbers)