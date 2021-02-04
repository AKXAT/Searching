def bubble_sort(mylist):
    size = len(mylist)
    for k in range(size-1):
        swapped = False 
        for i in range (size-1-k):
            if mylist[i]>mylist[i+1]:
                temp = mylist[i]
                mylist[i] = mylist[i+1]
                mylist[i+1]=temp
                swapped = True #this will tell us that if there was no swap then the list is already sorted
        if not swapped:
            break
    return mylist


if __name__ =='__main__':
    mylist = [3,5,1,2,3,89,0,4,34]
    #mylist = [0, 1, 2, 3, 3, 4, 5, 34, 89]
    print(bubble_sort(mylist))


    #output is [0, 1, 2, 3, 3, 4, 5, 34, 89]