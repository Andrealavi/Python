# Assignment: Create a script which asks the user to insert a number higher than 10.
# The script has to manage both the number <= 10 exception and not int input of the user exception

def numberInput():

    try:
        number = int(input('Insert a number >10: '))

        if number <= 10:
            raise Exception(
                "The number you've inserted is not higher than 10. Try again\n")

        return number
    except ValueError as error:
        print("You haven't inserted a number, please try again\n")
        numberInput()
    except Exception as error:
        print(error)
        numberInput()


print(numberInput())
