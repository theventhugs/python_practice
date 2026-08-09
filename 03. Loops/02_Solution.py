# Problem: Calculate the sum of even numbers up to a given number n.

# getting a number from the user
while(True):
    try:
        num = int(input("Enter the number till where you what the sum: ").strip())
        if num < 0:
            print("Please enter number greater than 0")
            continue
        break
    except Exception as ValueError:
        print("Enter a valid integer number")


# core logic
sum = 0
for i in range(1, num+1):
    if i % 2 == 0:
        sum += i

print(sum)