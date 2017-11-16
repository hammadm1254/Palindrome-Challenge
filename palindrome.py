import csv


def writeToCSV(data):
    """
    ## Write data to a CSV in current the current directory
    """
    with open('palindromeList.csv', "w") as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quoting=csv.QUOTE_MINIMAL)
        for key in data:
            writer.writerow([key, data[key]])


def is_Pal(aList):
    """
    ## This function checks a list of integers passed to it
    ## to check if it is palindrome. It check pairs of the
    ## first and last elements of the list in decrementing
    ## order. This cuts down the running time to O(n/2)
    """
    digitList = aList
    if type(digitList) != list or len(digitList) < 1:
        raise ValueError("Input must be non empty list of  integers")
    listSize = len(digitList)
    isPal = True
    i = 0
    while i < int(listSize / 2):
        if digitList[i] != digitList[(listSize - 1) - i]:
            isPal = False
            break
        else:
            i += 1
    return isPal


def to_Base(num, base):
    """
    ## Returns a list where each element represents
    ## the digit value in decimal integers for each
    ## digit of the number in the requested base.
    """
    if num < 0 or base < 2 or type(num) != int or type(base) != int:
        raise ValueError("Number must be an integer greater than 0 and base must be an integer greater than 2")
    digitList = [num % base]
    quotient = int(num / base)
    while quotient > 0:
        digit = quotient % base
        quotient = int(quotient / base)
        digitList.insert(0, digit)
    return digitList


def minimum_Base(number):
    """
    ## Takes an integer number as an argument
    ## and checks one by one if it is palindrome
    ## in a given base starting at base 2 to number + 1
    """
    if number < 1 or type(number) != int:
        raise ValueError("Number must be integer greater than zero")
    base = 2
    while base <= number + 1:  # plus 1 bc at worst a number is palindrome in the next base causing it to be single digit
        if is_Pal(to_Base(number, base)):
            return base
        else:
            base += 1


def Main():
    """
    ## This is the Main function. It uses an iterator function
    ## to generate a dictionary of integers and the finds the
    ## base in which it is palindrome
    """
    ## limit variable is the upper limit of numbers to be
    ## tested this must be a positive integer greater than 0
    limit = 1000
    palDict = {}
    num = iter(range(1, limit + 1))
    while True:
        try:
            temp = next(num)
            palDict[temp] = minimum_Base(temp)
        except StopIteration:
            break
    return palDict


if __name__ == '__main__':
    writeToCSV(Main())
    print("Finished writing data to palindromeList.csv")
    exit()
