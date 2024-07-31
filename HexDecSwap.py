
# Dictionary to convert a hex character into an integer
hexToDen = {
    "0" : 0,
    "1" : 1,
    "2" : 2,
    "3" : 3,
    "4" : 4,
    "5" : 5,
    "6" : 6,
    "7" : 7,
    "8" : 8,
    "9" : 9,
    "A" : 10,
    "B" : 11,
    "C" : 12,
    "D" : 13,
    "E" : 14,
    "F" : 15,
}

# Dictionary to convert an integer into a hex character
denToHex = {
    0 : "0",
    1 : "1",
    2 : "2",
    3 : "3",
    4 : "4",
    5 : "5",
    6 : "6",
    7 : "7",
    8 : "8",
    9 : "9",
    10 : "A",
    11 : "B",
    12 : "C",
    13 : "D",
    14 : "E",
    15 : "F",
}

def ConvertToDen(num):
    # Set exponent and return value
    exp = 0
    denNum = 0

    # Remove preceding 0x if it exists
    if num[1] == "x":
        num = num[2:]

    # Define the length of the hex number
    n = len(num)

    # Remove 'h' at the end of the number, if there is one
    if num[n-1] == "h":
        num = num[:n-1]
        n -= 1

    # Reverse the number for the loop
    num = num[::-1]

    # Loop through each character
    for i in range(0, n):
        # Multiply the character's corresponding number by 16 to the power of the current exponent and add to running total
        denNum += 16**exp * hexToDen[num[i]]

        # Increase the exponent for the next character
        exp += 1
    
    ## Return the total value
    return denNum


def ConvertToHex(num):
    hexNum = ""

    #Define list for remainders
    remainders = []

    # Record each remainder when the number is divided by 16
    while num != 0:
        remainders.append(num % 16)
        num //= 16

    # Reverse the remainders list as the hex number starts from the greatest power of 16
    remainders.reverse()

    # Get the corresponding hex character for each remainder from the dictionary
    for r in remainders:
        hexNum += denToHex[r]
    
    #  Return the hex number with preceding '0x'
    return "0x"+hexNum


## Start ##

# Test cases

num1 = "FF"
num2 = "0xF"
num3 = "Ah"
print(ConvertToDen(num1))
print(ConvertToDen(num2))
print(ConvertToDen(num3))

num4 = 1
num5 = 255
num6 = 4096
print(ConvertToHex(num4))
print(ConvertToHex(num5))
print(ConvertToHex(num6))