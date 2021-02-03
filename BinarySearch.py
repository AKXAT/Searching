def binary_search(mylist,value):
    left_index = 0
    right_index = len(mylist) - 1
    while left_index <= right_index : 
        mid_index = (left_index + right_index) // 2
        mid_number = mylist[mid_index]
        if mid_number == value:
            return mid_index
        if mid_number < value :
            left_index = mid_index + 1
        else:
            right_index = mid_index -1 
    return None 
if __name__ == '__main__' :
    mylist = [12,23,34,45,55,56,78,89,90]
    value = 550
    myfunc = binary_search(mylist,value)
    
    print(f"The value = {value} is present at the Index = {myfunc}")