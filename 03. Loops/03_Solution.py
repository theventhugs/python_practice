# Problem: Print the multiplication table for a given number up to 10, but skip the fifth iteration.

# getting a number from the user
while(True):
    try:
        num = int(input("Enter the number you want table of: ").strip())
        if num < 0:
            print("Please enter number greater than 0")
            continue
        break
    except Exception as ValueError:
        print("Enter a valid integer number")

# core logic
for i in range(1, 11):
    if i != 5:
        print(f"{num} X {i} =", num*i)