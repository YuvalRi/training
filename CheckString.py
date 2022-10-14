# ex7

with open('database.txt', mode='r') as f:
    contents = f.read()
if __name__ == "__main__":
    s = str(input("Please enter a word: "))
    if s in contents:
        print("The given word found")
    else:
        print("The given word is not found")


