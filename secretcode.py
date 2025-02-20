# TASK: Write a function that shifts each letter in a string by a given number.

# Define a function that takes a string and an integer shift value as parameters  
def codemaker(msg: str, shift: int) -> str:
# Create an empty list to store the shifted characters  
    code = []
# Loop through each character in the string:
    for x in msg:
        if x == int:
            code.append(x)
        else:
            code.append(ord(x))
    print(code)
        
#    If the character is a letter (A-Z or a-z):
    
#        Shift the letter by adding the shift value to its ASCII code (use the ord function)
#        Convert the new ASCII code back to a character (use the chr function)
#        Add the shifted character to the list
#    If the character is not a letter:
#        Add the character unchanged to the list
# After the loop, join the list into a string and return it  
# Get user input for the message and shift value  
msg = input("What is your message? ").strip()
shiftval = input("How many times would you like to shift it? ").strip()
# Call the function with the inputs and display the result
print(codemaker(msg, shiftval))