def linear_search(mylist,searching_for):
    for index,element in enumerate(mylist):
        if element == searching_for:
            return index 
    return -1

if __name__ == '__main__':
    mylist = [1,2,3,4,5,6,7,8,9]
    searching_for = 5
    print(f"The Element is present at the Index {linear_search(mylist,searching_for)} ")