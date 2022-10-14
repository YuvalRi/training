# ex5

if __name__ == "__main__":
    list = []
    for i in range(3):
        ele = int(input("Enter a number: "))
        list.append(ele)
    if len(set(list)) == 1:
        print(3*sum(list))
    else:
        print(sum(list))
