import random
random.seed(1, 25)

rdm1 = random.randint(1, 25)
rdm2 = random.randint(1, 25)
solution = rdm1 + rdm2
print("The task:", rdm1, "+", rdm2,)

number = solution + 1

trys = 0

while number != solution:
    trys = trys + 1
    print("Enter the solution:")
    i = input()
    number = int(i)

if number == solution:
    print(number, "is correct")
else:
    print("Attempt of trys:", trys)

print("Solution:", solution)
print("Amount of trys:",trys)