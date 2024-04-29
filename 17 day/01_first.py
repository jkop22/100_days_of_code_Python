# classes creation
# user of a web portal

class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0          # default attribute value
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1        

# user_1 = User()

# user_1.id = "A0001"
# user_1.username = "kopecny.jan@gmail.com"

# print(user_1, user_1.id)

user_1 = User("A001", "kopecny.jan@gmail.com")
print(user_1.id, user_1.username, user_1.followers)
# user_2 = User()     constructor attributes missing, so error
user_2 = User("B002", "john.doe@hotmail.com")
print(user_2.id, user_2.username, user_2.followers) 

# test metody 

user_1.follow(user_2)
user_2.follow(user_1)

attributes = dir(user_1)        # Get all attributes of the object

for attr in attributes:
    if not attr.startswith("__"):       # Exclude built-in attributes
        value = getattr(user_1, attr)   
        print(f"{attr}: {value}")
