# Personal Project by Bailey Schena
# Calculator

# Taking in a number
print("Please enter the first number")
numberOneInput = input("")
numberOne = int(numberTwoInput)

# Taking in a second number
print("Please enter the second number")
numberTwoInput = input("")
numberTwo = int(numberTwoInput)

# Choosing the operation
print("Please select an operation to perform with the two numbers.")
print("1. Add")
print("2. Multiply")
print("3. Subtract")
print("4. Divide")
userInputNum = input("Type in the corresponding number, and press enter: ")
userInput = int(userInputNum)

outputAnswer = 0

if userInput == 1:
    print("The answer is: ", numberOne + numberTwo)

elif userInput == 2:
    print("The answer is: ", numberOne * numberTwo)

elif userInput == 3:
    print("The answer is: ", numberOne - numberTwo)

elif userInput == 4:
    print("The answer is: ", numberOne / numberTwo)
