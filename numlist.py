numbers=input('adjal szamokat')

#numbers=numbers.split(',')

#for i in range(len(numbers)):
#    numbers[i]=int(numbers[i])

numbers=[int(i) for i in numbers.split(",")]

print(numbers)

for i in numbers:
    print('*'*i)