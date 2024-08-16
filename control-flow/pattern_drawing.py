size = int(input("Enter the size of the pattern: "))

row = 0

while row < size:

    for _ in range(size):
        print("*", end="")  # Print asterisk without moving to the next line
    
    print()
   
    row += 1
