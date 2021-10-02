#sum of three given numbers, if they are equal then we will get three times of their sum 
if __name__ == "__main__":
    lst = [] 
    for i in range(3):
        x = int(input("please insert a number: "))
        lst.append(x)

if  lst[0] == lst[1] == lst[2]:
    print(9*x)
else:
    print(sum(lst))
