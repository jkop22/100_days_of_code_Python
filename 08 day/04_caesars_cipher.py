alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

def caesar(msg, s_value, dir):
    secret = ""    
    
    if dir == "C":
        for i in msg:
            if i not in alphabet:
                secret += i
            elif alphabet.index(i) + s_value < len(alphabet):
                secret += alphabet[alphabet.index(i) + s_value]
            else:
                secret += alphabet[alphabet.index(i) - len(alphabet) + s_value]
        print(f"Encoded message is: {secret}")

    elif dir == "D":
        for i in msg:
            if i not in alphabet:
                secret += i
            elif alphabet.index(i) - s_value > 0:
                secret += alphabet[alphabet.index(i) - s_value]                               
            else:
                secret += alphabet[alphabet.index(i) - s_value + len(alphabet)] 
        print(f"Decoded message is: {secret}")

    else:
        print("Bad direction selection. Sorry.")    

from art import logo
print(logo)

rerun = True

while rerun == True:

    direction = input("\nDo you want to code or decode a message (C / D): ")
    message = input("Enter your message: ").lower()
    shift = int(input("Enter the shift number: "))
    shift = shift % 26

    caesar(message, shift, direction)

    again = input("\nDo U want to use me again? Y/N: ")
    if again == "N":
        rerun = False

print("Good Bye")