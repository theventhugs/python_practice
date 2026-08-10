# Problem: Write a function to calculate and return the square of a number.

def square(n):
    return (n*n)

def get_positive_int():
    while True:
        try:
            num = int(input("Enter a positive non-zero int: ").strip())
            if num < 1:
                print("number entered is not positive!")
                continue
            break
        except ValueError: # except Exception as ValueError: wiil catch all error => never goes to Exception as e
            print("Please enter a positive integral value")
        except Exception as e:
            print(e)

    return num

def main():
    num = get_positive_int()

    print(square(num))

if __name__ == "__main__":
    main()