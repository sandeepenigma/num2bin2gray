print("Number to Binary conversion")

num = int(input("Enter any number"))
quotient = num
binary = []
while quotient != 0:
    remainder = quotient%2
    binary = [remainder] + binary
    quotient = quotient//2


print(binary)

gray = [binary[0]]
lastindex = len(binary)-1
i=1

while  lastindex != 0:
    ngray = binary[i] ^ binary[i-1]
    gray += [ngray]
    i += 1
    lastindex -= 1

print("Gray code of above binary number",gray)