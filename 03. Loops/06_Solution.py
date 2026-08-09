# Problem: Compute the factorial of a number using a while loop.

# getting the correct value of n from the user
while(True):
    try:
        n = int(input("n? ").strip())
        if n < 0:
            print(f"factorial of {n} is not defined, please type value greater than or equal to 0")
            continue
        break
    except Exception as ValueError:
        print("please enter a valid integer value")

# core logic
fact = 1
while(n>1):
    fact *= n
    n = n-1

print(fact)