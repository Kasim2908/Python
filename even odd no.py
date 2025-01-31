# Function to check number is even
def is_even(number):
    if number % 2 == 0:
        return True
    else:
        return False

# taking input from user
num = int(input("Enter a number: "))

# Check if the number is even or not
if is_even(num):
    print(f"{num} is an even number.")
else:
    print(f"{num} is not an even number.")
