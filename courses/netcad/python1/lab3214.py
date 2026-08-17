blocks = int(input("Enter the number of blocks: "))

height = 0
block = 1

while blocks >= block:
    blocks -= block
    height += 1
    block += 1

print("The height of the pyramid:", height)