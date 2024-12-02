# 2. Take a user’s age as input and display whether they are a minor, adult, or senior citizen.


age = int(input("Enter your age: "))

# Check age category by using conditional statements.

if age < 18:
    print("You are a minor.")
elif 18 <= age <= 40:
    print("You are an adult.")
else:
    print("You are a senior citizen.")


# >>> You just need to enter your age like this: 
#     18, 30, 15, or 10... and then you will get your output like:

#     You are a minor ->> (15, 10) 
#     You are an adult ->> (18, 30)
#     You are a senior citizen ->> (If your age is above 40, you will get this output)