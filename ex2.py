import unittest


def ex1(string):                                             #Check if a string is a palindrome or not
    for i in range(len(string) // 2):
        if string[i] != string[-i - 1]:
            return ("The word is not a palindrome")
            return
    return ("The word is a palindrome")


def ex2(string):                                             #Find the longest word in a sentence
   newString = string.split()
   return (max(newString,key=len))


def ex3(firstString, secondString):                          #Check if two strings are anagrams of each other
    if(sorted(firstString.lower().replace(" ","")) == sorted(secondString.lower().replace(" ",""))):
        return "The given strings are anagrams of each other"
    else:
        return "The given strings are not anagrams of each other"

def ex4(number1, number2):                                   #Calculate the sum of two numbers
    return (number1+number2)


def ex5(numbers):                                                   #Calculate the average of a list of numbers
    num_of_numbers = len(numbers)
    total_sum = sum(numbers)
    return total_sum / num_of_numbers


#Unit Tests

class TestEx1(unittest.TestCase):

    def test_palindrome(self):
        self.assertEqual(ex1("racecar"), "The word is a palindrome")
        self.assertEqual(ex1("level"), "The word is a palindrome")
        self.assertEqual(ex1("deified"), "The word is a palindrome")
        self.assertEqual(ex1("rotator"), "The word is a palindrome")

    def test_not_palindrome(self):
        self.assertEqual(ex1("hello"), "The word is not a palindrome")
        self.assertEqual(ex1("world"), "The word is not a palindrome")
        self.assertEqual(ex1("python"), "The word is not a palindrome")


class TestEx2(unittest.TestCase):

    def test_longest_word(self):
        self.assertEqual(ex2("The quick brown fox jumps over the lazy dog"), "quick")
        self.assertEqual(ex2("I love coding in Python"), "coding")
        self.assertEqual(ex2("The longest word is antidisestablishmentarianism"), "antidisestablishmentarianism")


class TestEx3(unittest.TestCase):

    def test_anagrams(self):
        self.assertEqual(ex3("listen", "silent"), "The given strings are anagrams of each other")
        self.assertEqual(ex3("rail safety", "fairy tales"), "The given strings are anagrams of each other")
        self.assertEqual(ex3("Dormitory", "dirty room"), "The given strings are anagrams of each other")

    def test_not_anagrams(self):
        self.assertEqual(ex3("hello", "world"), "The given strings are not anagrams of each other")
        self.assertEqual(ex3("python", "java"), "The given strings are not anagrams of each other")


class TestEx4(unittest.TestCase):

    def test_sum(self):
        self.assertEqual(ex4(5, 10), 15)
        self.assertEqual(ex4(-2, 3), 1)
        self.assertEqual(ex4(0, 0), 0)


class TestEx5(unittest.TestCase):

    def test_calculate_average(self):
        self.assertAlmostEqual(ex5([1, 2, 3, 4, 5]), 3.0)
        self.assertAlmostEqual(ex5([0, 0, 0, 0, 0]), 0.0)
        self.assertAlmostEqual(ex5([-1, 0, 1]), 0.0)


if __name__ == '__main__':
    unittest.main()
