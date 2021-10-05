#even or odd?
if __name__ == "__main__": 
    x = int(input("please enter a number: ")) #a number which given by the user
    if x%2 == 0: #using modulo operator to classify whether x is even or odd
        print(f'The given number is even!')
    else:
        print(f'The given number is odd!')
