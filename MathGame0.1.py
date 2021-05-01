import random
random.seed()

rdm1 = random.randint(1, 10)
rdm2 = random.randint(1, 10)
solution = rdm1 + rdm2
print("The task:" , rdm1, "+" , rdm2,)

print("Enter the solution:")

x = input()
number = int(x)

if number == solution:
    print(number, "is correct")
else:
    print("Solution: ", solution)