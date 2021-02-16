def romanToInt(s: str) -> int:
    number_hash = {
        "I" : 1,
        "V" : 5,
        "IV" : 4,
        "IX" : 9,
        "XL" : 40,
        "X" : 10,
        "L" : 50,
        "XC": 90,
        "C" : 100, 
        "CD" : 400,
        "D" : 500, 
        "CM": 900,
        "M" : 1000,
    }

    integer = 0
    index = 0
    
    while index < len(s):
        if index < len(s) - 1 and s[index:index+2] in number_hash:
            integer += number_hash[s[index:index+2]]
            index += 2
        else:
            integer += number_hash[s[index]]
            index += 1
            
    return integer
