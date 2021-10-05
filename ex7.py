if __name__ == "__main__":
    f = open("WordData.txt", "r")
    readf = f.read()

    x = input("please enter a string: ")

    if x in readf:
        print("The string2 appears in the dataset!")
    else:
        print("The string does not appear in the dataset!") 