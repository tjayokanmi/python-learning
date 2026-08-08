#print("Hello, World!")

# name = input("What's your name? ").strip().title()

# #removing space from the right and left from str
# name = name.strip()

# #print("Hello, " + NAME)

# #print("Hello,", NAME)

# # Capitalize the first word in a string
# #name = name.capitalize()

# #capitalize the first character of each word in a string 
# #name = name.title()

# #name = name.strip().title()

# print(f"Hello, {name}") 

# def hello(to="world"):
#     print("Hello,", to)

# hello()
# name = input("What's your name? ")
# hello(name)

def main():
    name = input("What's your name? ")
    hello(name)

def hello(to="world"):
    print("Hello,", to)

main()