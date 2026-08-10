# Problem: Write a function to calculate and return the square of a number.

def square(n):
    return (n*n)

def get_positive_int(message, zero="N"):
    while True:
        try:
            num = int(input(message).strip())
            if num < 0:
                print("number entered is not positive!")
                continue
            elif num == 0 and zero == "N":
                print("Zero is not allowed")
                continue
            break
        except ValueError: # except Exception as ValueError: wiil catch all error => never goes to Exception as e
            print("Please enter a positive integral value")
        except Exception as e:
            print(e)

    return num

def main():
    num = get_positive_int("Enter a number to be squared: ")

    print(square(num))

if __name__ == "__main__":
    main()