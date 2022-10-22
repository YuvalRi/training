# ex5
# a - program to filter values from dictionary based on a specific condition

if __name__ == "__main__":
    dict = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
    new_dict = {}
    for key, value in dict.items():
        if dict[key] > 170:
            new_dict[key] = value
    print(new_dict)

# b


def filterValues(dict: dict):
    '''
    function to filter values from dictionary based on a specific condition
    '''
    new_dict = {}
    for key, value in dict.items():
        if dict[key] > 170:
            new_dict[key] = value
    return new_dict


if __name__ == "__main__":
    dict = {'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
    print(filterValues(dict))
