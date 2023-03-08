
def ex6():                                             #Check if a string is a palindrome or not
    string = input("Insert a word:")
    for i in range(len(string) // 2):
        if string[i] != string[-i - 1]:
            print("The word is not a palindrome")
            return
    print ("The word is a palindrome")


def ex7():                                             #Find the longest word in a sentence
   string = input("Input a sentence:")
   newString = string.split()
   print(max(newString,key=len))


def ex8():                                             #Check if two strings are anagrams of each other
    firstString = input("Input first string:")
    secondString = input("Input second string:")
    if(firstString == secondString):
        print("The given strings are anagrams of each other")
    else: print("The given strings are not anagrams of each other")


def ex9():                                             #Calculate the sum of two numbers
    number1 = int(input("Input first number:"))
    number2 = int(input("Input second number:"))
    print(number1+number2)


def ex10():                                            #Calculate the average of a list of numbers
    nrOfNumbers = int(input("Input number of numbers:"))
    sum = 0
    nr = {}
    for i in range(nrOfNumbers):
        nr[i] = int(input("Input number:"))
        sum = sum + nr[i]
    print("The average is:",(sum/nrOfNumbers))
