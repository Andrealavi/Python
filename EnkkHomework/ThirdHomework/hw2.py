# Assignment: write a main() function which will be used to test other minor functions:
#     - rev(list): takes a list and print it reversed
#     - isPositive(n): takes a number and returns True if the number is positive and false if it is negative
#     - a funtion which takes a list and remove duplicates
#     - a function which takes a string and see if it's palindrome. It returns True or False
#     - a function which takes a number and returns its factorial

def rev(list):
    return list[::-1]


def isPositive(n):
    if n > 0:
        return True
    return False


def duplicateRemover(list):
    return [element for element in list if list.count(element) == 1]


def palindromeFinder(string):
    if string == string[::-1]:
        return True
    return False


def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n*factorial(n-1)


def main():
    list = ['ciao', 'ciao', 'come', 'stai', 'come', 'ciao']
    number = 5
    string = 'bob'

    print("Let's try some functions \n\n\n")
    print("Let's try 'rev function': ", rev(list))
    print("Let's try 'isPositive function': ", isPositive(number))
    print("Let's try 'duplicateRemover function': ", duplicateRemover(list))
    print("Let's try 'palindromeFinder function': ", palindromeFinder(string))
    print("Let's try 'factorial function': ", factorial(number))


main()
