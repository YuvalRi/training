#exercise 4 - concatenating following dictionaries to create a new one
if __name__ == "__main__":
    dic1 = {1:10, 2:20} #sample dictionary
    dic2 = {3:30, 4:40}
    dic3 = {5:50, 6:60}
    new_dict = dic1.update(dic2)
    new_dict2 = dic1.update(dic3)
    print(dic1)
