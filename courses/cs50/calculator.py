# # x = input("What's x " )

# # y = input("What's y  ?" )

# # z = int(x) + int(y)

# x = float(input("What's X? "))
# y = float(input("What's Y? "))

# # z = round(x + y)
# z = x/y

# # print(f"{z:,}")

# print(f"{z:.4f}")

def main():
    x = int(input("what's X? "))
    print("x squared is", square(x))

def square(n):
    return n * n

main()