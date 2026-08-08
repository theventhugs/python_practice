# Classify a person's age group: Child (< 13), Teenager (13-19), Adult (20-59), Senior (60+).

# get the valid age from the user
while(True):
    try:
        age = int(input("Enter your age: "))
        if age < 1:
            print("enter value greater than zero")
            continue
        if age > 130:
            print("Enter realistic age")
            continue
        break
    except Exception as ValueError:
        print("Please enter an integer number greater than 0")
    
# main classification logic
if age < 13:
    print("You are a child")
elif 13 <= age <= 19:
    print("You are a teenager")
elif 20 <= age <= 59:
    print("You are a Adult")
elif age >= 60:
    print("You are a Senior")