#Mapping the roman to the integer
def value(r):
    if (r == 'I'):
        return 1
    if (r == 'V'):
        return 5
    if (r == 'X'):
        return 10
    if (r == 'L'):
        return 50
    if (r == 'C'):
        return 100
    if (r == 'D'):
        return 500
    if (r == 'M'):
        return 1000
    return -1

#Checking the validity of the roman number
def checkIfRomanNumeral(numeral):
        #Importing the regex library
        import re
        #Uppercasing the input variable
        numeral = numeral.upper()
        #List for valid roman numerals
        validRomanNumerals = ["M", "D", "C", "L", "X", "V", "I"]
        #for each letters in the input, checking for validity
        for letters in numeral:
            if letters not in validRomanNumerals:
                print("Sorry that is not a valid roman numeral")
                exit()
        #Checking for logical validity of roman number
        valid_ = bool(re.search(r"^M{0,3}(CM|CD|D?C{0,3})(XC|XL|L?X{0,3})(IX|IV|V?I{0,3})$", numeral))
        if valid_ == False:
            print("The roman number is not valid")
            exit()
        return romanToInteger()


#Code to convert roman to integer
def romanToInteger(str):
    #result and i are 0 at beginning
    res = 0
    i = 0

    #while i is upto the length of the string
    while (i < len(str)):
        #extracting the value of 1st letter
        s1 = value(str[i])
        #if the next character is available
        if (i + 1 < len(str)):
            #extract the value of next character
            s2 = value(str[i + 1])
            #if current character is greater than next character or equal, add the value in result
            if (s1 >= s2):
                res = res + s1
                i = i + 1
            #or else subtract the next character value with current character value and add in result
            else:
                res = res + s2 - s1
                i = i + 2
        else:
            res = res + s1
            i = i + 1

    return res

#test every sort of cases
conv = input("Enter the roman number to be converted to integer")
result = checkIfRomanNumeral(conv)
print("The roman number for %s is %d" %(conv,result))