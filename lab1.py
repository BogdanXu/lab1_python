from math import gcd
from functools import reduce

# Find The greatest common divisor of multiple numbers read from the console.
def problem_1():
    def readNumbers():
        list_of_numbers = []
        n = int(input('Enter the number of numbers you want to calculate the gcd to:'))
        index = 0
        while index<n:
            list_of_numbers.append(int(input('Enter the number:')))
            index=index+1
        return list_of_numbers
    def cmmdc():
        numbers = readNumbers()
        result = reduce(gcd, numbers) #chestia asta apeleaza gcd pe primele 2, apoi pe rezultat si urmatorul numar
        print(result)
    cmmdc()

# Write a script that calculates how many vowels are in a string.
def problem_2():
    inputString = "helloworld"
    vowels = "aeiou"
    numberOfVowels = 0
    for index in range(0, len(inputString)):
        if vowels.find(inputString[index], 0, 4)>=0:
            print("found vowel", inputString[index])
            numberOfVowels=numberOfVowels+1
    print(numberOfVowels)

#Write a script that receives two strings and prints the number of occurrences of the first string in the second.
def problem_3():
    count = 0
    inputString1 = "ana"
    inputString2 = "banana ana analfabet katana"
    for index in range(0, len(inputString2)):
        if inputString2.find(inputString1, index, index+3)>=0:
            count = count + 1
            index = index + 2
    print(count)

#Write a script that converts a string of characters written in UpperCamelCase into lowercase_with_underscores.
def problem_4():
    inputString = "CamelCamelCamel"

    inputString = inputString.replace(inputString[0], inputString[0].lower())

    for index in range(1, len(inputString)):
        if inputString[index].isupper():
            #print("found uppercase", inputString[index])
            aux = "_" + inputString[index].lower()
            #print("letter to replace uppercase is", aux)
            inputString = inputString.replace(inputString[index], aux)
    print(inputString)

#Given a square matrix of characters write a script that prints the string obtained by going through the matrix in spiral order (as in the example):

def problem_5():
    squareMatrix = ["firs",
                    "n_lt",
                    "oba_",
                    "htyp"]

    size = len(squareMatrix[0])
    rightPoint = size
    downPoint = size
    leftPoint = 0
    upPoint = 0
    result = ""
    while leftPoint<size/2:
        for index in range(leftPoint, rightPoint):
            result = result + squareMatrix[upPoint][index]     #prima linie, f -> s
        upPoint = upPoint + 1
        for index in range(upPoint, downPoint):
            result = result + squareMatrix[index][rightPoint-1] #ultima coloana, t -> p
        rightPoint = rightPoint - 1
        for index in range(rightPoint-1, leftPoint-1, -1):
            result = result + squareMatrix[downPoint-1][index]  #ultima linie, y -> h
        downPoint = downPoint - 1
        for index in range(downPoint-1, upPoint-1, -1):
            result = result + squareMatrix[index][leftPoint]    #prima coloana, o -> n
        leftPoint = leftPoint + 1

    print(result)

# Write a function that validates if a number is a palindrome.
def problem_6():
    def palindrome(number: int):
        length = len(str(number))
        number = str(number)
        isPalindrome = 1
        for index in range(0, length//2):
            if(number[index]!=number[length - index - 1]):
                print(number, "is not a palindrome")
                isPalindrome = 0
        if(isPalindrome == 1):
            print(number, "is a palindrome")
    palindrome(1)

# Write a function that extract a number from a text (for example if the text is "An apple is 123 USD", this function will
# return 123, or if the text is "abc123abc" the function will extract 123). 
# The function will extract only the first number that is found.


def problem_7():
    def findFirstNumber():
        inputstring = "abc123abc123512asgasgasg125521 asdasd 1245"
        foundnumber = 0
        result = ""
        for index in range(0, len(inputstring)):
            if inputstring[index].isnumeric():
                result = result + inputstring[index]
                foundnumber = 1
            if foundnumber == 1 and not inputstring[index].isnumeric():
                print(result)
                break
    findFirstNumber()

#Write a function that counts how many bits with value 1 a number has. For example for number 24, the binary format is 00011000, meaning 2 bits with value "1"

def problem_8():
    def countBits():
        inputnumber = 4095
        counter = 0
        binary = bin(inputnumber)
        binary = str(binary)
        binary = binary[2:]
        print("The binary conversion of", inputnumber, "is", binary)
        for index in range(0, len(binary)):
            if binary[index]=='1':
                counter+=1
        print(counter)
    countBits()

# Write a functions that determine the most common letter in a string. For example if the string is "an apple is not a tomato", then the most common character is "a" (4 times).
# Only letters (A-Z or a-z) are to be considered. Casing should not be considered "A" and "a" represent the same character.

def problem_9():
    def findCommonLetter():
        inputstring = "a tomAYto is a tomAto not a potatooooooooooooo"
        inputstring = inputstring.lower()
        frequency = 26*[0]          #inmultiri de vectori lmao
        max = 0
        char = ""
        for character in inputstring:
            if character.islower():
                i = ord(character)-ord('a')
                frequency[i]+=1
        for index in range(0, 26):
            if frequency[index]>max:
                max = frequency[index]
                char = chr(index+65)
        print("The most common letter is", char, "with", max, "apparitions")
    findCommonLetter()
problem_9()
        
