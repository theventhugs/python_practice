# Problem: Movie tickets are priced based on age: $12 for adults (18 and over), $8 for children. Everyone gets a $2 discount on Wednesday.


# getting a valid current day from the user
days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
while(True):
    day = input("Enter today's day: ")
    if day.lower() in days:
        break
    else:
        print(f"Enter valid day from {days}")

# Getting a valid age from the user
while(True):
    try:
        age = int(input("Enter you age: "))
        if age < 0:
            print("Enter age greater than zero")
            continue
        if age > 130:
            print("Enter a realistic age")
            continue
        break
    except Exception as ValueError:
        print("Please enter an integer number greater than 0")

# The core logic
price = 0

if age < 18:
    price = 8
else:
    price = 12

if day == "wednesday":
    price -= 2

print("Final price to be paid:", price)