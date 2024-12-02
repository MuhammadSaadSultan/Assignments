# 2. Create a function to generate a random password of given length, 
# containing uppercase, lowercase, numbers, and special characters.


import random
import string

def generate_password(length):  
    if length < 4:
        raise ValueError("Password length must be at least 4 characters")
    
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    digits = string.digits
    special_characters = string.punctuation
    
    password = [
        random.choice(uppercase),
        random.choice(lowercase),
        random.choice(digits),
        random.choice(special_characters)
    ]
    
    all_characters = uppercase + lowercase + digits + special_characters
    password += random.choices(all_characters, k=length - 4)
    
    random.shuffle(password)
    
    return ''.join(password)

password = generate_password(12)
print(password)



# The code creates a random password with a mix of uppercase letters, lowercase 
# letters, numbers, and special symbols. It makes sure there’s at least one of each type, 
# then shuffles everything so the password is random and hard to guess.