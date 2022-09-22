def most_common_value(number_list):
    """ returns the most common element of the list
    """
    counter = 0
    num = number_list[0]
     
    for i in number_list:
        frequency = number_list.count(i)
        if(frequency> counter):
            counter = frequency
            num = i
 
    return num


if __name__ == "__main__":
    nums = [1, 1, 3, 3, 3, 7, 8, 2, 1, 3]
    print(f"Most common value = {most_common_value(nums)}")
