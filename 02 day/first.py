print("Hello"[0]) # H
print("Hello"[1:]) # ello
print("Hello"[1:4]) # ell
print("Hello"[-1]) # o
print("Hello"[:-1]) # Hell

print("123" + "456") # concatenation
print(123 + 456) # matematicke scitani

pi = 3.1415928 # primitivni typ float
is_married = False # primitivni typ boolean

len("12345") # OK
# len(12345)  error bo používáme len() na ne-string

num_char = str(len(input("What is your name? ")))
print("Your name has " + num_char + " characters.")

print(type(num_char))