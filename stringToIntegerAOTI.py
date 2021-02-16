def myAtoi(s):
    if s == "" or s == "+" or s == "-":
        return 0
    
    stringtoList = [i for i in s]
    
    if not stringtoList[0].isdigit() and not stringtoList[1].isdigit():
        return 0
        
    newString = [i for i in stringtoList if i is not " "]

    positive =  True
    stringtoIngeger = ""
    
    if newString[0] == ".":
        return 0
    
    if "-" in newString:
        positive = False
    
    if any(number.isalpha() for number in stringtoIngeger):
        if number not "-" or number not "+":
            return 0
    
    if not positive:
        stringtoIngeger += "-"
        
    for char in newString:
        if not char.isdigit():
            if char == ".":
                break
            else:
                continue  
        else:
            stringtoIngeger += str(char)
        
    if int(stringtoIngeger) < pow(-2,31):
        return pow(-2,31)
    
    elif int(stringtoIngeger) > (pow(2,31)-1):
        return (pow(2,31)-1)
    
    return int(stringtoIngeger) 


# return 0
print(myAtoi(""))

# return 0
print(myAtoi("+"))

# return 0
print(myAtoi("-"))

# returns 42
print(myAtoi("0000042"))

# returns -42
print(myAtoi("       -42"))

# returns 4193
print(myAtoi("4193 with words"))

# returns 0
print(myAtoi("words and 987"))

#returns -2147483648 due to lower limit being clamped
print(myAtoi("-91283472332"))

# returns 3
print(myAtoi("3.21512312"))

print(myAtoi(".1"))