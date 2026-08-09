# Problem: Suggest an activity based on the weather (e.g., Sunny - Go for a walk, Rainy - Read a book, Snowy - Build a snowman).

# getting weather from the user
print("Press 1 for Sunny | Press 2 for Rainy | Press 3 for Snowy")
while(True):
    try:
        wether = int(input("What's the wether aound you? "))
        if wether in [1, 2, 3]:
            break
        else:
            print("Please select either 1, 2 or 3")
    except Exception as ValueError:
        print("Please enter only integer value from 1, 2, or 3")


    
# Core logic 
if wether == 1:
    print("Go for a walk")
elif wether == 2:
    print("Read a book")
else:
    print("Build a snowman")