#height of pyramid
blocks = int(input("Enter the number of blocks: "))
# Write your code here.
height = 0
inlayer = 1
while inlayer <= blocks:
    height += 1
    blocks -= inlayer
    inlayer += 1

print("The height of the pyramid:", height)