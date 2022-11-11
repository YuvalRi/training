#reversed user's first and last name
import re

def rev(x):
    st = x.split(" ")
    return(" ".join(reversed(st)))
    
if __name__ == "__main__":
    x = input("please enter your first name and last name: ")
    print(rev(x))