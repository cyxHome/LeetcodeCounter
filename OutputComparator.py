def parseListListString(filename):
    """ Parse a List<List<String>> string from file

        Input: a string
        Return: an array, each entry of which is an array of string,
                elements in the inner array has been sorted in ascending order
    """
    fr = open(filename, 'r')
    origin = fr.read()
    parsed = origin.split("],[")
    a = []
    for entry in parsed:
        tmp = entry.split("\"")
        res = []
        for i in range(len(tmp)):
            if (i % 2 == 1):
                res.append(tmp[i])
        res.sort()
        a.append(res)
    a.sort()
    fr.close()
    return a

def compareTwoArray(input1, input2):
    """ Check if two arrays has the same elements

        Input: two arrays
        Return: no return
        Effect: print the result of checking to the console
    """
    equal = True
    print "------------------------------"
    for i in range(len(input1)):
        if (input1[i] not in input2):
            print input1[i], "is not in file input2.txt"
            equal = False
    if (not equal):
        print "------------------------------"
    for i in range(len(input2)):
        if (input2[i] not in input1):
            print input2[i], "is not in file input1.txt"
            equal = False
    if (equal):
        print "Two Arrays Are Equal!"

def checkListListString():
    """ Check a List<List<String>> string from file input1.txt and input2.txt
        are equivalent. If not print the difference.

        Usage: store the first string to check in filename1
               store the first string to check in filename2
               filename1 and filename2 should be in the same folder as
               this python script.
               
    """
    quit = raw_input(("You want to check if two List<List<String>>"
                    "strings are equal?\n(y/n): "))
    if (quit == 'y' or quit == 'yes' or quit == 'Y'):
        input1 = raw_input("Your first file's name: ")
        input2 = raw_input("Your second file's name: ")

        compareTwoArray(parseListListString(input1),
                        parseListListString(input2))

if __name__ == "__main__":
    checkListListString()
