# Problem: Assign a letter grade based on a student's score: A (90-100), B (80-89), C (70-79), D (60-69), F (below 60).

# getting a valid score from student
while(True):
    try:
        score = int(input("Enter you marks: ").strip())
        if score < 0:
            print("Score you entered is lesser than zero")
            continue
        if score > 100:
            print("Score you entered is greater than 100")
            continue
        break
    except Exception as ValueError:
        print("Enter an integer value")

# The core logic
if score >= 90:
    Grade = "A"
elif 80 <= score <= 89:
    Grade = "B"
elif 70 <= score <= 79:
    Grade = "C"
elif 60 <= score <= 69:
    Grade = "D"
else:
    Grade = "F"
print(f"You grade is {Grade}, as per your obtained marks")