def bubble_sort(mylist):
    size = len(mylist)
    for k in range(size-1):
        for i in range (size-1-k):
            if mylist[i]>mylist[i+1]:
                temp = mylist[i]
                mylist[i] = mylist[i+1]
                mylist[i+1]=temp
        
    return mylist


if __name__ =='__main__':
    mylist = [3,5,1,2,3,89,0,4,34]
    print(bubble_sort(mylist))