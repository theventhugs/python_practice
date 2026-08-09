# Problem: Check if a password is "Weak", "Medium", or "Strong". Criteria: < 6 chars (Weak), 6-10 chars (Medium), >10 chars (Strong).

# getting password as input
password = input("Password: ").strip()

# getting number of characters from password
chars = len(password)

# finding strength of password based on the question's requirements
strength = ""
if chars < 6:
    strength = "Weak"
elif 6 <= chars <= 10:
    strength = "Medium"
else:
    strength = "Strong"

# getting output
print("Your password strength is: ", strength)