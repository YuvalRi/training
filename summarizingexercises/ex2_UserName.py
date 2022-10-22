# ex2
# A program which accepts the user's first and last name and reverse its order
if __name__ == "__main__":
    x = str(input("Please enter your full name:"))
    x = ' '.join(reversed(x.split()))
    print(x)
