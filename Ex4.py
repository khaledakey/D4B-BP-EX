user_input = input("Enter your number: ")

try: 
    number = float(user_input)
    print(f"You entered the number: {number}")
    print (f"Type: {type(number)}")
except ValueError:
    print("Invalid input. Please enter a valid number.")