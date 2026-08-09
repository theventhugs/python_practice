# Problem: Given a string, find the first non-repeated character.

string = input("Enter a string you want to get inverse of: ").strip()

for index, char in enumerate(string):
    if char not in string[:index] and char not in string[index+1:]:
        print(char)


# input_str = "teeteracdacd"

# for char in input_str:
#     print(char)
#     if input_str.count(char) == 1:
#         print("Char is: ", char)
#         break