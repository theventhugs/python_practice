# Problem: Check if a number is prime.

def main():
    # getting the correct value of n from the user
    while(True):
        try:
            n = int(input("n? ").strip())
            if n < 1:
                print("Enter value greater than zero")
                continue
            break
        except Exception as ValueError:
            print("please enter a valid integer value")

    check_prime(n)


# core logic 
def check_prime(n):
    till_check = int(n/2)

    for i in range(2, till_check+1):
        if n % i == 0:
            print("Not a prime number")
            return
    print("Prime number")
    return

if __name__ == "__main__":
    main()