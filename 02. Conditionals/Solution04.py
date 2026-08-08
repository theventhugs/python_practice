# Problem: Determine if a fruit is ripe, overripe, or unripe based on its color. (e.g., Banana: Green - Unripe, Yellow - Ripe, Brown - Overripe)

# getting color for banana from the user
print("Press 1 for Green | Press 2 for Yellow | Press 3 for Brown")
while(True):
    try:
        color = int(input("What colour is you banana: "))
        if color in [1, 2, 3]:
            break
        else:
            print("Please select either 1, 2 or 3")
    except Exception as ValueError:
        print("Please enter only integer value")


    
# Core logic 
if color == 1:
    print("It's Unripe")
elif color == 2:
    print("It's Ripe")
else:
    print("It's Overipe")