# Initiailize the programm with Number Boundaries
S = int(input("Enter Number to Start interval : "))
E = int(input("Entet Number To End interval : "))
print("The Prime numbers between", S, "and", E, "are :")
# Loop for find Prime number in given range(S & E)
for n in range(S,E):
  if n>1:         # Prime Number is greater than 1
    for m in range(2, n):
        if(n % m == 0):      # To check if reminder of division =0
            break
    else:
        print(n)

