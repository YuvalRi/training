# ex7

def readFile(name):
    '''
    function for opening a txt file for reading text
    '''
    f = open(name, mode='r')
    contents = f.read()
    return contents


def stringCheck(words, s: str):
    '''
    function for checking if a string is founded in the above txt file
    '''
    if s in words:
        print("The given word was found")
    else:
        print("The given word was not found")


def main():
    contents = readFile('database.txt')
    s = str(input("Please enter a word: "))
    stringCheck(contents, s)


if __name__ == "__main__":
    main()
