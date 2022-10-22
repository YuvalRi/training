# ex5
# A program to calculate the sum of three given numbers.
# if the values are equal, the program will returns three times of their sum.

if __name__ == "__main__":
    list = []
    for i in range(3):
        ele = int(input("Enter a number: "))
        list.append(ele)
    if len(set(list)) == 1:
        print(3*sum(list))
    else:
        print(sum(list))
