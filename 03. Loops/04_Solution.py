# Problem: Reverse a string using a loop.

string = input("Enter a string you want to get inverse of: ").strip()

inverted_string = ""
length = len(string)

# for i in range(length-1, -1, -1):
#     inverted_string += string[i]
for char in string:
    inverted_string = char + inverted_string  

print(inverted_string)

